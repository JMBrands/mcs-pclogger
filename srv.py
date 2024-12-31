#!/usr/bin/env python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 25565))

s.listen(1)

while True:
    (clientsocket, address) = s.accept()

    buf = clientsocket.recv(1024)
    if len(buf) > 0:
        print(buf)