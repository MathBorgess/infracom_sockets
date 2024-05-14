from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 8000))
for _ in range(3):
    client.send('Hello, World!'.encode())
    print(client.recv(1024).decode())
client.close()