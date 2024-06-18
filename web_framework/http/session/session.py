import json
import os.path
import uuid
import time


class Session:
    def __init__(self, session_id=None, storage_path='sessions', expiry=3600):
        self.session_id = session_id or str(uuid.uuid4())
        self.storage_path = storage_path
        self.expiry = expiry
        self.data = self.load_session()

    def load_session(self):
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
        session_file = os.path.join(self.storage_path, f"{self.session_id}.json")
        if os.path.isfile(session_file):
            with open(session_file, 'r') as file_handler:
                session_data = json.load(file_handler)
                if time.time() - session_data.get('timestamp', 0) > self.expiry:
                    self.delete_session()
                    return {}
                return session_data.get('data', {})
        return {}

    def save_session(self):
        session_file = os.path.join(self.storage_path, f"{self.session_id}.json")
        session_data = {
            'timestamp': time.time(),
            'data': self.data
        }
        with open(session_file, 'w') as file_handler:
            json.dump(session_data, file_handler)

    def delete_session(self):
        session_file = os.path.join(self.storage_path, f"{self.session_id}.json")
        if os.path.isfile(session_file):
            os.remove(session_file)
        self.data = {}

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_session()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_session()

    def clear(self):
        self.data = {}
        self.save_session()
