# client.py
import socket, sys, time, random, pickle, functions

# Booting
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Create the socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Fetch IPv4 of user
self_ip = "127.0.0.1"
self_port = 8080
self_tcp = (self_ip, self_port)

server_ip = input("Enter server IPv4: ")
server_port = int(input("Enter server port: "))

server = (server_ip, server_port)
print(f"\nTrying to connect to {server}...\n")
tcp_socket.connect(server)

# Send welcome message
message = functions.send(tcp_socket, b"START")
end = functions.recv(tcp_socket)

tcp_socket.close()
