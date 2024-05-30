from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import sys
from threading import Thread

port = int(sys.argv[1])
port_dst = int(sys.argv[2])


def handle_sender():
    print('Sending message to', port_dst)
    sender = socket(AF_INET, SOCK_STREAM)
    while True:
        try:
            sender.connect(('localhost', port_dst))
            msg = sender.recv(1024).decode()
            print(msg)
            break
        except ConnectionRefusedError:
            sender = socket(AF_INET, SOCK_STREAM)
    while True:
        while True:
            msg = input()
            if msg == 'exit':
                sender.send(msg.encode())
                sender.close()
                break
            else:
                sender.send(msg.encode())


def handle_reciever():
    reciever = socket(AF_INET, SOCK_STREAM)
    reciever.bind(('localhost', port))
    print('Listening on', port)
    reciever.listen()
    while True:
        c, addr = reciever.accept()
        print('Got connection from', addr)
        c.send('Thank you for connecting'.encode())
        while True:
            msg = c.recv(1024).decode()
            print(msg)
            if msg == 'exit':
                break
        c.close()


Thread(target=handle_reciever).start()
Thread(target=handle_sender).start()
