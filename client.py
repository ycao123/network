# client.py
import socket, sys, time, random, pickle, functions

# Booting
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Create the socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Fetch IPv4 of user
self_ip = "127.0.0.1"
self_port = 8000
self_tcp = (self_ip, self_port)

server_ip = input("Enter server IPv4: ")
server_port = int(input("Enter server port: "))

server = (server_ip, server_port)
print(f"\nTrying to connect to {server}...\n")

##try:
##    tcp_socket.connect(server)
##except:
##    print("Invalid information")
##    sys.exit(1)
tcp_socket.connect(server)

while True:
    data = [self_ip, "CONNECT"]
    data_binary = pickle.dumps(data)
    tcp_socket.sendto(data_binary, server)

# Send welcome message
message = s.recv(1024)
message = message.decode()
client_ip = message
print("Received connection from ", message, ")\n")
print("Client: ", message)

# Repeat forever or until client sends [e]
while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Client left"
        conn.send(message.encode())
        print("\n")
        break
    s.sendto(message.encode(), (client_ip,4000))
    message = s.recv(1024)
    message = message.decode()
    print("Client: ", message)
