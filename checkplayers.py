#!/usr/bin/env python3
import socket
import json

def checkplayers(settings: dict):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((settings["server"], settings["port"]))
    s.send(b'\x10\x00\xFF\x05\x09localhost\63\xDD\x01')
    s.send(b'\x00')
    s.send(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00')
    s.settimeout(0.5)
    status = b""
    data = s.recv(10)
    while True:
        status += data
        try:
            data = s.recv(4069)
        except TimeoutError:
            break

    status = status[status.find(b'{'):]

    status = json.loads(status)

    return status["players"]["online"]
