'''
Functions and macros for TCP chat
'''

# Built-in modules
import pickle
import socket
import sys

try:
    import netifaces
except:
    netifaces = None

# Macros
SERVER_PORT = 24680

def get_gateway_ip():
    "Gets the gateway/public IPv4"
    if netifaces:
        en0_addr = netifaces.ifaddresses("en0")
    else:
        print("netifaces not found. Consider using 'python3 -m pip3 install netifaces'")
        sys.exit(1)
    inet_addr = en0_addr[2]
    self_addr = inet_addr[0]['addr']
    gateway_addr = inet_addr
    print("Self address: ", self_addr)
    return gateway_addr

def get_ip():
    "Gets the local IPv4"
    self_ip = socket.gethostbyname(socket.gethostname())
    return self_ip

def start(mode):
    # Booting
    print("\nWelcome to Chat Room\n")
    print("Initialising....\n")

    # Create the socket
    tcp_socket = socket.socket()

    # Selects mode
    # Server mode
    if mode.lower() == "server":
        # Modify socket to server
        self_ip = socket.gethostname()
        self_tcp = (self_ip, SERVER_PORT)
        tcp_socket.bind(self_tcp)

        # Set to listen(5)
        tcp_socket.listen(5)

        # Listen for connection
        print(f"Serving on {self_tcp}")
        print("IPv4: ", get_ip())
        print("\nWaiting for connection...\n")

        return tcp_socket

    # Client mode
    elif mode.lower() == "client":

        # Modify socket to client
        self_ip = "0.0.0.0"
        SELF_PORT = 12345
        self_tcp = (self_ip, SELF_PORT)
        tcp_socket.bind(self_tcp)

        # Get server IP
        server_ip = input("Enter server IPv4: ")

        server = (server_ip, SERVER_PORT)
        print(f"\nTrying to connect to {server}...\n")
        tcp_socket.connect(server)
        
        return tcp_socket

    else:
        print("Not a mode")
        tcp_socket.close()
        sys.exit(2)

def receive(tcp_socket):
    "Receives message from tcp_socket"
    recv = tcp_socket.recv(1024)
    message = pickle.loads(recv).decode()
    return message

def send(tcp_socket, text):
    "Sends message 'text' with tcp_socket"
    data = pickle.dumps(text)
    tcp_socket.send(data)

print("IPv4", get_ip())