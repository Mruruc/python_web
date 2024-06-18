from .session import Session
from ..cookie import Cookie


class SessionMiddleware:
    def __init__(self, storage_path='sessions'):
        self.storage_path = storage_path

    def process_request(self, request):
        session_id = request.get_cookie("session_id")
        if session_id:
            request.session = Session(session_id=session_id, storage_path=self.storage_path)

    def process_response(self, request, response):
        if request.session:
            request.session.save_session()
            response.set_cookie(Cookie(name="session_id", value=request.session.session_id))
