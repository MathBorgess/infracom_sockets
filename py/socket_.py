from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
#
# SOCK_STREAM: TCP
# SOCK_DGRAM: UDP
#

listener = socket(AF_INET, SOCK_STREAM)

listener.bind(('localhost', 8000))
listener.listen()

client, addr = listener.accept()
while true:
    req  = client.recv(1024)
    print(req.decode())

    client.send('Hello, World from Py!'.encode())
