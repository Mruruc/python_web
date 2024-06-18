from socket import *


def create_server():
    server = socket(AF_INET, SOCK_STREAM)
    try:
        server.bind(('localhost', 9000))
        server.listen(1)  # The server should listen for incoming connections
        print("Server listening on port 9000...")

        while True:
            (client, address) = server.accept()
            print(client, client.getsockname())
            print(address)
            request = client.recv(5000)
            print(request.decode())

            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html;charset=utf-8\r\n\r\n"
            response += "<html><body> <h1>Hello there ...</h1></body></html>"

            client.sendall(response.encode())
            client.shutdown(SHUT_WR)
            client.close()
    except KeyboardInterrupt:
        print("\nShutting Down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    finally:
        print("Server is shutting down.....")
        server.close()


create_server()
