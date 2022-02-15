'''
Client for the TCP chat
'''

import socket
import functions
# Booting up the chat room
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

tcp_socket = functions.start("client")

# Connected!
print("Connected!")

# Send welcome message
functions.send(tcp_socket, b"START")
end = functions.receive(tcp_socket)
print(end)

# End the TCP session
tcp_socket.close()
