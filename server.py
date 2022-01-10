# server.py
import socket, sys, time, random, pickle
import functions

# Booting
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Create the socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creates the socket tuple
self_ip = "10.153.61.239"
self_port = 8000
print("Port: ", self_port)
self_tcp = (self_ip, self_port)

# Binds to the host and port
tcp_socket.bind(self_tcp)
print("TCP socket: ", self_tcp)

# Prints the gateway/public IPv4
print("FOR TEST. TRY BOTH IPS")
functions.get_gateway_ip()

print("\nWaiting for connection...\n")

# Listens for any incoming connections
tcp_socket.listen()
    
conn, addr = tcp_socket.accept()

with conn:
    print("Connected by ", addr)
    recv = functions.recv(conn)
    functions.send(conn, b"END")

tcp_socket.close()
