from .exceptions.http_protocol_exceptions import HttpMethodNotSupportedException


class RequestMapping:

    def handle_http_request_response(self, request, response):
        request_method = request.method.strip().upper()

        if request_method == 'GET':
            self.get_mapping(request, response)

        elif request_method == 'POST':
            self.post_mapping(request, response)

        elif request_method == 'PUT':
            self.put_mapping(request, response)

        elif request_method == 'DELETE':
            self.delete_mapping(request, response)
        else:
            raise HttpMethodNotSupportedException(f'Http method is not supported {request_method}')

    def get_mapping(self, request, response):
        pass

    def post_mapping(self, request, response):
        pass

    def put_mapping(self, request, response):
        pass

    def delete_mapping(self, request, response):
        pass

    def forward_to(self, request, response, new_path):
        if request.router:
            request.router.forward(request, response, new_path)
        else:
            response.status_code = 500
            response.response_content_string("Internal Server Error: Router not found")
