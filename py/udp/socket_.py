from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM


listener = socket(AF_INET, SOCK_DGRAM)

listener.bind(('localhost', 11708))

while True:
    data, addr = listener.recvfrom(1024)
    print(f'Received: {data.decode()} from {addr}')
