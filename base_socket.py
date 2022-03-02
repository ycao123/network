'''
Creates client and server
'''

import socket
from subprocess import check_output, STDOUT
import sys
import random

SERVER_PORT = 2345

def chmod(file, permission=755):
    "Changes file permissions"
    check_output(["ls", "-l", file], stderr=STDOUT)
    check_output(["chmod", str(permission), file], stderr=STDOUT)
    check_output(["ls", "-l", file], stderr=STDOUT)

class BaseSocket:
    "The base for the client and server sockets"
    def __init__(self, addr, port) -> None:
        self.tcp_socket = socket.socket()
        self.addr = addr
        self.port = port
        self.self_ip = (self.addr, self.port)
        self.tcp_socket.bind(self.self_ip)
        print("Bound to: ", self.self_ip)

    def send(self, data):
        "Sends data"
        self.tcp_socket.send(data)

    def recv(self, socket_type):
        "Receives data"
        data = socket_type.recv(4096)
        print(f"Received {data}")
        return data
    def close(self):
        "Closes the socket"
        self.tcp_socket.close()
        print("Closed socket")

class ClientSocket(BaseSocket):
    "The client socket"
    def __init__(self, addr="0.0.0.0") -> None:
        # Gets the base elements
        super().__init__(addr, random.randint(2096, 2344))
        self.tcp_socket.settimeout(10)
        self.server = ()
    def connect(self, server) -> None:
        "Connects to server"
        self.server = server
        self.tcp_socket.connect(self.server)
        print("Connected to ", self.server)
    def recv(self):
        value = super().recv(self.tcp_socket)
        return value

class ServerSocket(BaseSocket):
    "The server socket"
    def __init__(self) -> None:
        # Maybe change to get_ip if this doesn't work
        super().__init__("0.0.0.0", SERVER_PORT)
        self.conn = ""
        print("ServerSocket Called!")
        self.tcp_socket.listen(5)

    def listen(self) -> None:
        "Listens for connection"
        print("Started listening!")
        self.conn, self.return_addr = self.tcp_socket.accept()
        print("Connected by", self.return_addr)

    def send(self, data) -> None:
        self.conn.send(data)
    def recv(self):
        value = super().recv(self.conn)
        return value


def main():
    "Main function"
    try:
        if sys.argv[1] == "client":
            client_socket = ClientSocket()
            client_socket.connect((input("Enter Server IPv4: "), SERVER_PORT))
        elif sys.argv[1] == "server":
            server_socket = ServerSocket()
            server_socket.listen()
    except BaseException as some_error:
        print(some_error)

if __name__ == "__main__":
    main()
