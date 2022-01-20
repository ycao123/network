# Built-in modules
import requests 
import socket 
import pickle
import sys

# Pip-installed modules
try:
    import netifaces
except ImportError:
    print("Missing these modules:\nnetifaces")

# Gets the gateway/public IPv4
def get_gateway_ip():
    en0_addr = netifaces.ifaddresses("en0")
    inet_addr = en0_addr[2]
    gateway_addr = inet_addr[0]['broadcast']
    print(gateway_addr)
    return gateway_addr

# Gets local IPv4
def get_ip():
    "Gets the local IPv4 of the "
    ip = socket.gethostbyname(socket.gethostname())
    print("IPv4: ", ip)
    return ip

def recv(tcp_socket):
    recv = tcp_socket.recv(1024)
    message = pickle.loads(recv).decode()
    print(message)
    return message

def send(tcp_socket, text):
    data = pickle.dumps(text)
    tcp_socket.send(data)
