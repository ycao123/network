'''
Creates client and server
'''

import socket
import sys

SERVER_PORT = 23456

def get_ip():
    "Gets the local IPv4"
    self_ip = socket.gethostbyname(socket.gethostname())
    return self_ip

class BaseSocket:
    "The base for the client and server sockets"
    def __init__(self, addr, port):
        print("\nWelcome to Chat Room\n")
        print("Initialising....\n")
        self.tcp_socket = socket.socket()
        self.addr = addr
        self.port = port
        self.ip = (self.addr, self.port)
        self.tcp_socket.bind(self.ip)
        print("Bound to: ", self.ip)

class ClientSocket(BaseSocket):
    "The client socket"
    def __init__(self):
        # Gets the base elements
        super().__init__("0.0.0.0", 12345)
        print("ClientSocket Called!")
    def connect(self) -> None:
        "Connects to server"
        self.server = (input("Enter server IPv4: "), SERVER_PORT)
        print("Server: ", self.server)
        self.tcp_socket.connect(self.server)
        print("Connected to ", self.server)

class ServerSocket(BaseSocket):
    "The server socket"
    def __init__(self):
        # Maybe change to get_ip if this doesn't work
        super().__init__(get_ip(), SERVER_PORT)
        print("ServerSocket Called!")
        self.tcp_socket.listen(5)
        self.connected = False

    def listen(self) -> None:
        "Listens for connection"
        print("Started listening!")
        self.conn, self.addr = self.tcp_socket.accept()
        print("Connected by", self.addr)
        self.connected = True


if sys.argv[1] == "client":
    a = ClientSocket()
    a.connect()
elif sys.argv[1] == "server":
    a = ServerSocket()
    a.listen()

