from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from threading import Thread
#
# SOCK_STREAM: TCP
# SOCK_DGRAM: UDP
#


def handle_client(client):
    req = client.recv(1024)
    print(req.decode())

    client.send('Hello, World from Py!'.encode())
    client.close()


listener = socket(AF_INET, SOCK_STREAM)

listener.bind(('localhost', 8000))
listener.listen()

while True:
    client, addr = listener.accept()
    Thread(target=handle_client, args=(client,)).start()
