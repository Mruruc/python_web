import socket

http_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http_client.connect(("127.0.0.1", 8080))
http_client.send('POST /login http://127.0.0.1 HTTP/1.0\r\n\r\n'.encode())

while True:
    response = http_client.recv(512)
    if len(response) < 1:
        break
    print(response.decode())

http_client.close()