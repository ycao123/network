'''
Client for the TCP chat
'''

import socket
import functions
#from tcp_socket import __all__
# Booting up the chat room
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Start the tcp_socket
tcp_socket = functions.start(1)

# Connected!
print("Connected!")

# Send welcome message
functions.send(tcp_socket, b"START")
end = functions.receive(tcp_socket)
print(end)

# End the TCP session
tcp_socket.close()
