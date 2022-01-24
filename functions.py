'''
Functions and macros for TCP chat
'''

# Built-in modules
import pickle
import requests
import netifaces

# Macros
SERVER_PORT = 8000

def get_gateway_ip():
    "Gets the gateway/public IPv4"
    en0_addr = netifaces.ifaddresses("en0")
    inet_addr = en0_addr[2]
    gateway_addr = inet_addr[0]['broadcast']
    print(gateway_addr)
    return gateway_addr

def get_ip():
    "Gets the local IPv4"
    self_ip = socket.gethostbyname(socket.gethostname())
    print("IPv4: ", self_ip)
    return ip

def receive(tcp_socket):
    recv = tcp_socket.recv(1024)
    message = pickle.loads(recv).decode()
    return message

def send(tcp_socket, text):
    data = pickle.dumps(text)
    tcp_socket.send(data)
