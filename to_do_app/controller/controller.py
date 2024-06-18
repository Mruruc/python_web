from web_framework.http.http_status_code import *
from web_framework.request_mapping import RequestMapping


class HomeController(RequestMapping):
    def get_mapping(self, request, response):
        response.add_header("Content-Type", "text/html;charset=utf-8")
        response.template('/to_do_app/views/index.html')


class LoginController(RequestMapping):
    def get_mapping(self, request, response):
        response.add_header("Content-Type", "text/html;charset=utf-8")
        response.template('/to_do_app/views/login.html')

    def post_mapping(self, request, response):
        user_name = request.get_request_attribute('userName')
        password = request.get_request_attribute('password')

        user_name = user_name.split('@')[0]
        request.set_session()
        request.session.set("username", user_name)
        request.session.set("userId", 25466)

        response.redirect('/todos')

    def put_mapping(self, request, response):
        session_id = request.body
        if session_id and hasattr(request, 'session') and request.session.session_id == session_id:
            request.session.delete_session()
        response.redirect("/")


class ToDoController(RequestMapping):
    def get_mapping(self, request, response):
        response.add_header("Content-Type", "text/html;charset=utf-8")
        response.template('/to_do_app/views/todos.html')

    def post_mapping(self, request, response):
        pass


class NotFoundController(RequestMapping):
    def get_mapping(self, request, response):
        response.add_header("Content-Type", "text/html;charset=utf-8")
        response.status_code = NOT_FOUND
        response.template('/to_do_app/views/not_found.html')
