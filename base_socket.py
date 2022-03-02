'''
Creates client and server
'''

import socket
from subprocess import check_output, STDOUT
import sys
import random

SERVER_PORT = 23456

def chmod(file, permission=755):
    check_output(["ls", "-l", file], stderr=STDOUT)
    check_output(["chmod", str(permission), file], stderr=STDOUT)
    check_output(["ls", "-l", file], stderr=STDOUT)

class BaseSocket:
    "The base for the client and server sockets"
    def __init__(self, addr, port) -> None:
        self.tcp_socket = socket.socket()
        self.addr = addr
        self.port = port
        self.ip = (self.addr, self.port)
        self.tcp_socket.bind(self.ip)
        print("Bound to: ", self.ip)
    def send(self, data):
        self.tcp_socket.send(data)
    def recv(self):
        data = self.tcp_socket.recv(4096)
        return data
    def close(self):
        self.tcp_socket.close()
        print("Closed socket")

class ClientSocket(BaseSocket):
    "The client socket"
    def __init__(self, addr="0.0.0.0") -> None:
        # Gets the base elements
        super().__init__(addr, random.randint(2096, 12345))
    def connect(self, server) -> None:
        "Connects to server"
        self.server = server
        self.tcp_socket.connect(self.server)
        print("Connected to ", self.server)

class ServerSocket(BaseSocket):
    "The server socket"
    def __init__(self) -> None:
        # Maybe change to get_ip if this doesn't work
        super().__init__("0.0.0.0", SERVER_PORT)
        print("ServerSocket Called!")
        self.tcp_socket.listen(5)

    def listen(self) -> None:
        "Listens for connection"
        print("Started listening!")
        self.conn, self.addr = self.tcp_socket.accept()
        print("Connected by", self.addr)

try:
    if sys.argv[1] == "client":
        a = ClientSocket()
        a.connect(input("Enter Server IPv4: "))
    elif sys.argv[1] == "server":
        a = ServerSocket()
        a.listen()
except BaseException as e:
    print(e)
