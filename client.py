'''
Client for the TCP chat
'''
import socket
from functions import send, receive, SERVER_PORT

# Booting up the chat room
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Create the socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.settimeout(3)


# Fetch IPv4 of user
self_ip = socket.gethostname()
self_port = 12345
self_tcp = (self_ip, self_port)

# Ask for server IP
server_ip = input("Enter server IPv4: ")

# Try to connect to server
server = (server_ip, SERVER_PORT)
print(f"\nTrying to connect to {server}...\n")
tcp_socket.connect(server)

# Connected!
print("Connected!")

# Send welcome message
send(tcp_socket, b"START")
end = receive(tcp_socket)
print(end)

# End the TCP session
tcp_socket.close()
