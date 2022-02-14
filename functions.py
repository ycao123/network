'''
Functions and macros for TCP chat
'''

# Built-in modules
import pickle
import socket
import netifaces

# Macros
SERVER_PORT = 8000

def get_gateway_ip():
    "Gets the gateway/public IPv4"
    en0_addr = netifaces.ifaddresses("en0")
    inet_addr = en0_addr[2]
    self_addr = inet_addr[0]['addr']
    gateway_addr = inet_addr
    print("Self address: ", self_addr)
    return gateway_addr

def get_ip():
    "Gets the local IPv4"
    self_ip = socket.gethostbyname(socket.gethostname())
    print("IPv4: ", self_ip)
    return self_ip

def receive(tcp_socket):
    "Receives message from tcp_socket"
    recv = tcp_socket.recv(1024)
    message = pickle.loads(recv).decode()
    return message

def send(tcp_socket, text):
    "Sends message 'text' with tcp_socket"
    data = pickle.dumps(text)
    tcp_socket.send(data)
