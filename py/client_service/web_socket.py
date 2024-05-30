from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from threading import Thread
#
# SOCK_STREAM: TCP
# SOCK_DGRAM: UDP
#


def handle_client(client):
    req = client.recv(1024)
    print(req.decode())
    msgHeader = 'HTTP/1.1 200 OK \r\n' \
        'Date: Tue, 09 Aug 2022 13:23:35 GMT\r\n' \
        'Server: MyServer/0.0.1 (Ubuntu)\r\n' \
        'Content-Type: text/html\r\n' \
        '\r\n'
    msgBody = '<html>' \
        '<head><title>Hello, World</title></head>' \
        '<body><h1> Your first web server!</h1>' \
        '<h3>Congratulation!!</h3>' \
        '</body>' \
        '</html>'

    client.send((msgHeader + msgBody).encode())
    client.close()


listener = socket(AF_INET, SOCK_STREAM)

listener.bind(('localhost', 8000))
listener.listen()

while True:
    client, addr = listener.accept()
    Thread(target=handle_client, args=(client,)).start()
