#!/usr/bin/python3

import socket
import json

with open("./conf.json", 'r') as f:
    config = json.load(f)


HOST = config["ap_ctrl"]["ip"]  # The server's hostname or IP address
PORT = config["ap_ctrl"]["port"]  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))