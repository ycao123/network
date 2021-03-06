'''
Server for TCP chat
'''

import socket

from socket import gethostname as get_ip
import functions

# Booting
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Start the tcp_socket
tcp_socket = functions.start("server")

conn, addr = tcp_socket.accept()

try:
    with conn:
        print("Connected by ", addr)
        recv = functions.receive(conn)
        functions.send(conn, b"END")
    
    conn.getpeername()
# OSerror
except Exception as error:
    print(str(error))

finally:
    print("Thank you for joining!")
    conn.close()
    tcp_socket.close()