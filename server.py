'''
Server for TCP chat
'''

import socket
from functions import get_gateway_ip, receive, send, SERVER_PORT

# Booting
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Create the socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creates the socket tuple
self_ip = socket.gethostname()
print("Port: ", SERVER_PORT)
self_tcp = (self_ip, SERVER_PORT)

# Binds to the host and port
tcp_socket.bind(self_tcp)
print("\nIP address: ", self_ip)
print("\nTCP socket: ", self_tcp)

# Prints the gateway/public IPv4
print("FOR TEST. TRY BOTH IPS")
get_gateway_ip()

print("\nWaiting for connection...\n")

# Listens for any incoming connections
tcp_socket.listen()

conn, addr = tcp_socket.accept()

with conn:
    print("Connected by ", addr)
    recv = receive(conn)
    send(conn, b"END")
    
tcp_socket.getpeername()
tcp_socket.close()
