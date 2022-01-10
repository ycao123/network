import requests, socket, pickle, sys, netifaces
from cryptography.fernet import Fernet

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

# NO CLUE
def receive_message(conn):
    message = pickle.loads(conn.recv(1024))
    message_type = type(message)
    if isinstance(message_type, type(list)):
        time.sleep(1)
        print("Received Data!")
        return list((True, message))
    else:
        time.sleep(1)
        return list((False, "ERROR"))

def recv(tcp_socket):
    recv = tcp_socket.recv(1024)
    message = pickle.loads(recv).decode()
    print(message)
    return message

def send(tcp_socket, text):
    data = pickle.dumps(text)
    tcp_socket.send(data)
    
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

def send_text(text):
    data = pickle.dumps(text)
    udp_socket.sendto(data, server)

def send_file(filename):
    with open(file, "r"):
        data = file.read()
    send_text(data)

# message = encrypt(["json.format", 1, {"1" : (0,1)}], key)
# print(message)
# print(decrypt(message, key))
