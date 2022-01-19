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
#from cryptography.fernet import Fernet

default_key = b'D_nB_gRXA6AjnbHDuIYyj74XFx8X8YlVWns1_4qF_sY='

# Gets the gateway/public IPv4
def get_gateway_ip():
    en0_addr = netifaces.ifaddresses("en0")
    inet_addr = en0_addr[2]
    gateway_addr = inet_addr[0]['broadcast']
    print(gateway_addr)
    return gateway_addr

# Gets local IPv4
def get_ip():
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
'''   
# Encrypts a message
def encrypt(text, key):
    fernet = Fernet(key)
    message = fernet.encrypt(pickle.dumps(text))
    return message

# Decrypts a message
def decrypt(text, key):
    fernet = Fernet(key)
    message = pickle.loads(fernet.decrypt(text))
    return message

# Generates a key to use for encryption/decryption
def generate_key():
    answer = input("Generate key (default is no)? [yes/no] ")
    if answer == "yes":
        key = Fernet.generate_key().decode()
        print("Key: ", key)
    else:
        key = default_key
    return key

# Loads a key for encryption/decryption
def load_key():
    answer = input("Load key (default is no)? [yes/no] ")
    if answer == "yes":
        key = input("Key: ").encode()
        if len(key) != 44:
            print("Invalid Key")
            sys.exit(2)
    else:
        key = default_key
    return key
'''
