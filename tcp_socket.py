'''
Creates client and server
'''

from functions import SERVER_PORT
import socket

class BaseSocket:
    def __init__(self, addr, port):
        print("\nWelcome to Chat Room\n")
        print("Initialising....\n")
        self.tcp_socket = socket.socket()
        self.addr = addr
        self.port = port
        self.ip = (self.addr, self.port)
        self.tcp_socket.bind(self.ip)
        print("Bound to: ", self.ip)

    def get_ip(self):
        "Gets the local IPv4"
        self_ip = socket.gethostbyname(socket.gethostname())
        return self_ip

class ClientSocket(BaseSocket):
    def __init__(self):
        # Gets the base elements
        super().__init__("0.0.0.0", 12345)
        print("Hi!")

    
class ServerSocket(BaseSocket):
    def __init__(self):
        # Maybe change to get_ip if this doesn't work
        super().__init__("0.0.0.0", SERVER_PORT)

b = ServerSocket()