import socket

socket_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_socket.connect(('data.pr4e.org', 80))
request = 'GET http://data.pre4e.org HTTP/1.0\r\n\r\n'

socket_socket.send(request.encode())

file_handler = open("test.html", 'a')

while True:
    data = socket_socket.recv(512)

    if len(data) < 1:
        break
    file_handler.write(data.decode())

file_handler.close()
socket_socket.close()
