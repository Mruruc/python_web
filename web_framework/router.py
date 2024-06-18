from web_framework.http.request import Request
from web_framework.http.response import Response
from web_framework.exceptions.forward_redirect_exceptions import ControllerNotFoundException
from .http.session.session_middleware import SessionMiddleware


class Router:
    def __init__(self):
        self.controller = dict()
        self.middleware = SessionMiddleware(storage_path="")

    def add_controller(self, path, controller):
        self.controller[path] = controller

    def route(self, request_info_map):
        request = Request(
            request_info_map['method'],
            request_info_map['path'],
            request_info_map['headers'],
            request_info_map.get('body_data'),
            router=self,
            cookies=request_info_map.get('cookies')
        )
        response = Response()
        self.middleware.process_request(request)

        print("Request Path ==>>", request_info_map['method'], request_info_map['path'])
        controller = self.controller.get(request_info_map['path'], self.controller.get('/else'))
        print('request and response passed to  ==>', controller, "controller")

        controller.handle_http_request_response(request, response)

        self.middleware.process_response(request, response)

        return response

    def forward(self, request, response, new_path):
        new_controller = self.controller.get(new_path)
        if new_controller:
            new_controller.handle_http_request_response(request, response)
        else:
            raise ControllerNotFoundException(f"Controller for {new_path} Not Found!")
