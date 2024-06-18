from urllib import request

handler = request.urlopen('http://127.0.0.1:9000/')

for line in handler:
    print(line.decode())


