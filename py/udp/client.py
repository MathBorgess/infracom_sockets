from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from time import sleep

clients = []
for _ in range(3):
    clients.append(socket(AF_INET, SOCK_DGRAM))
# Aniversário em 17 de Agosto, 1708
for client_code in range(9):
    sleep(1)
    clients[client_code % 3].sendto(
        f'Hello, server from {(client_code % 3) + 1} client!'.encode(), ('localhost', 11708))
for client in clients:
    client.close()
