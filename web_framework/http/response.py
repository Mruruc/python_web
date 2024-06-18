from web_framework.http.http_status_code import OK


class Response:
    def __init__(self, status_code=OK):
        self.status_code = status_code
        self.headers = {}
        self.body = ''
        self.attribute = dict()
        self.cookies = []

    def template(self, view_path):
        try:
            with open(view_path, 'r') as file_handler:
                self.body = file_handler.read()
                self.add_header("Content-Length", len(self.body))
        except Exception as exc:
            self.status_code = 500
            self.body = f"Internal Server Error: {exc}"
            print(exc)

    def add_header(self, header, value):
        self.headers[header] = value

    def set_cookie(self, cookie):
        self.cookies.append(str(cookie))

    def render(self):
        header_str = f"HTTP/1.1 {self.status_code} \r\n"
        for key, value in self.headers.items():
            header_str += f"{key}: {value}\r\n"
        for cookie in self.cookies:
            header_str += f"Set-Cookie: {cookie}\r\n"
        header_str += "\r\n"
        return header_str + self.body

    def response_content_string(self, content):
        self.body = content
        self.add_header("Content-Length", str(len(self.body)))

    def redirect(self, url):
        self.status_code = 302
        self.add_header('Location', url)
        self.body = f"HTTP/1.1 302 Found\r\nLocation: {url}\r\n\r\n"
