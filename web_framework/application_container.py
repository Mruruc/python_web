from socket import *
from .utils.request_response_util import extract_request_info
from .router import Router


class AppContainer:

    def __init__(self, ip_addr='127.0.0.1', port=8080):
        self.router = Router()
        self.ip_addr = ip_addr
        self.port = port

    def routes(self, path, controller):
        self.router.add_controller(path, controller)

    def handle_client(self, client):
        try:
            request = client.recv(5000).decode()
            request_map = extract_request_info(request)
            response = self.router.route(request_map).render().encode()
            client.sendall(response)
        except Exception as exc:
            print(f"Error handling client request: {exc}")
        finally:
            client.shutdown(SHUT_WR)
            client.close()

    def run(self):
        server = socket(AF_INET, SOCK_STREAM)
        try:
            server.bind((self.ip_addr, self.port))
            server.listen(5)
            print(f"Server listening on port {self.port}...")

            while True:
                client, address = server.accept()
                self.handle_client(client)
        except KeyboardInterrupt:
            print("Shutting Down...")
        except Exception as exc:
            print(f"Server error: {exc}")
        finally:
            print("Server is shutting down...")
            server.close()
