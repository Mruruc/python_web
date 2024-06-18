from email.utils import formatdate

from model import User
from web_framework.jwt_utils import *
from web_framework.request_mapping import RequestMapping


class ToDoController(RequestMapping):
    def get_mapping(self, request, response):
        auth_header = request.get_header('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            response.add_header("Status", "Forbidden")
            response.status_code = 401
            return response.response_content_string(json.dumps(
                {
                    "error": "Unauthorized"
                }
            ))

        token = auth_header.split(" ")[1]
        payload_ = verify_jwt(token)

        if payload_ is None:
            response.status_code = 401
            return response.response_content_string(json.dumps({"error": "Unauthorized"}))

        response.add_header("Content-Type", "application/json")
        with open("db.json", "r") as f_h:
            result = f_h.read()
        return response.response_content_string(result)

    def post_mapping(self, request, response):
        user_dict = json.loads(request.body)
        user = User(user_dict.get('username'), user_dict.get('password'))

        with open("db.json", "a") as file_handler:
            file_handler.write(request.body)

        jwt_token = generate_jwt(
            "HS256", {
                "user_id": "65555",
                "username": user.username
            }
        )
        response.add_header("Content-Type", "application/json")
        response.add_header("Authorization", f"Bearer {jwt_token}")
        response.add_header("Location", f"http:/")
        response.add_header("Cache-Control", "no-cache, no-store, must-revalidate")
        response.add_header("Date", formatdate(timeval=None, localtime=False, usegmt=True))

        response.status_code = 201
