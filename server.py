# server.py
# LOOK AT IFCONFIG EN0 BROADCAST
import socket, sys, time, random, pickle
import functions

# Booting
print("\nWelcome to Chat Room\n")
print("Initialising....\n")

# Create the socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creates the socket tuple
self_ip = "10.153.61.239"
#self_port = random.randint(49152,65535)
self_port = 8080
print("Port: ", self_port)
self_tcp = (self_ip, self_port)

# Binds to the host and port
tcp_socket.bind(self_tcp)
print("TCP socket: ", self_tcp)

# Prints the gateway/public IPv4
print("FOR TEST. TRY BOTH IPS")
functions.get_gateway_ip()

# Generates the key for encryption/decryption
# key = functions.generate_key()

# Listens for any incoming connections
tcp_socket.listen(1)
print("\nWaiting for connection...\n")


conn, addr = tcp_socket.accept()

with conn:
    print("Connected by ", addr)

def receive_message():
    message = pickle.loads(conn.recv(4096))
    message_type = type(message)
    if isinstance(message_type, type(list)):
        time.sleep(1)
        print("Received Data!")
        print(message)
        return list(message)
    else:
        time.sleep(1)
        return list("ERROR")

def send_text(text, ip):
    data = pickle.dumps(text)
    tcp_socket.sendto(data, ip)

def send_file(filename, ip):
    with open(file, "r"):
        data = file.read()
    send_text(data, ip)

# Repeat forever or until client sends [e]
while True:
    data = receive_message()
    if data[1] == "CONNECT":
        client_ip = (data[0], 8080)
        clients.append(client_ip)
        message = data[1]
        print(f"\nReceived connection request from {client_ip}")
        print(f"Accepted connection request from {client_ip}\n")
        print(f"Sending CONNECTION_APPROVED\n\n")
        send_text(["SERVER", "CONNECTION_APPROVED"], client_ip)
    elif data[1] == "":
        message = input(str("Me : "))
        if message == "[e]":
            message = "Client left"
            conn.send(message.encode())
            print("\n")
            break
    else:
        udp_socket.sendto(message, client_ip)
        message = s.recv(1024)
        message = message.decode()
        print("Client: ", message)
