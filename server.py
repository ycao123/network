'''
Server for TCP chat
'''

import socket

from socket import gethostname as get_ip, gethostbyname
from functions import get_gateway_ip, receive, send, SERVER_PORT

# Booting
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Create the socket
tcp_socket = socket.socket()

# Creates the socket tuple
self_ip = socket.gethostname()
self_tcp = (self_ip, SERVER_PORT)

# Binds to the host and port
tcp_socket.bind(self_tcp)
tcp_socket.listen(5)

# Prints the gateway/public IPv4
print(f"Serving on {self_tcp}")
print("Ip: ", get_ip())

print("\nWaiting for connection...\n")

# Listens for any incoming connections
tcp_socket.listen()

conn, addr = tcp_socket.accept()
try:
    with conn:
        print("Connected by ", addr)
        recv = receive(conn)
        send(conn, b"END")
    
    conn.getpeername()
except OSError as error:
    print("OSError: ", str(error))
except:
    pass
finally:
    print("Thank you for joining!")
    conn.close()
