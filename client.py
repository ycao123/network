import socket
import sys
import time
import random
import pickle
import functions

# Booting
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Create the socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Fetch IPv4 of user
self_ip = socket.gethostname()
self_port = random.randint("1024", "2047")
self_tcp = (self_ip, self_port)

server_ip = input("Enter server IPv4: ")
server_port = 8000

server = (server_ip, server_port)
print(f"\nTrying to connect to {server}...\n")
tcp_socket.connect(server)

print("Connected!")

# Send welcome message
message = functions.send(tcp_socket, b"START")
end = functions.recv(tcp_socket)

tcp_socket.close()
