from .session.session import Session


class Request:
    def __init__(self, method, path, headers, body, router=None, cookies=None, session=None):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body
        self.router = router
        self.cookies = cookies
        self.session = session

    def set_session(self):
        self.session = Session()
        self.session.save_session()
        self.set_cookie('session_id',self.session.session_id)

    def get_cookie(self, key):
        return self.cookies.get(key) if self.cookies is not None else None

    def set_cookie(self, key, value):
        if self.cookies:
            self.cookies[key] = value
        else:
            self.cookies = {key: value}

    def get_request_attribute(self, key):
        return self.body.get(key)

    def get_header(self, key):
        return self.headers.get(key)
