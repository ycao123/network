'''
The GUI builder for the chat
'''

# Imports
import tkinter as tk
import sys
from ipaddress import ip_address
from base_socket import BaseSocket, ClientSocket, ServerSocket, SERVER_PORT

class Chat:
    "The main Chat class"
    def __init__(self, tcp_socket) -> None:
        "Initialize the Chat"

        # Sees if it is a subclass of BaseSocket
        if not issubclass(type(tcp_socket), BaseSocket):
            raise AttributeError(
                "Error: Please make sure to use ClientSocket or ServerSocket for the tcp_socket"
                )
        # Self variables
        self.tcp_socket = tcp_socket
        self.server_ip = ["", SERVER_PORT]
        self.window = tk.Tk()
        self.window.title("Chat Room")
        self.connected = False
        self.frame = tk.Frame(self.window)
        self.exit_button = tk.Button(self.frame, text="Terminate session", command=self.quit)
        self.main_window = tk.Text(self.frame, height=50, width=60, bg="#d3d2fa")
        self.entry_window = tk.Text(self.frame, height=5, width=80, bg="#c4f5cc")
        self.submit_button = tk.Button(self.frame, text="Submit", command=self.send)
        self.refresh_button = tk.Button(self.frame, text="Receive", command=self.update)
        self.counter = 1
        self.main_window.configure(state="disabled")


        # Starts the correct options
        if isinstance(self.tcp_socket, ClientSocket):
            self.chat_client()
        else:
            self.chat_server()

    def get_server(self):
        "Asks for the server"
        # Starting the window
        server_tk = tk.Tk()
        server_tk.geometry("400x150")
        server_tk.title("Please enter server IPv4")

        # The widgets
        lbl_message = tk.Label(master=server_tk, text="Enter Server IPv4: ")
        ent_entry = tk.Entry(master=server_tk)
        btn_submit = tk.Button(master=server_tk,
                               text="Submit",
                               command=lambda: self.server_ent_quit(server_tk,
                                                                    ent_entry))
        # Packing/running them
        lbl_message.pack()
        ent_entry.pack()
        btn_submit.pack()

        server_tk.mainloop()

    def server_ent_quit(self, master, ent=None) -> None:
        "The quit fucntion for the get_server() function"
        if ent:
            text = ent.get()
        try:
            if ent:
                ip_address(text)
                self.server_ip[0] = text
                master.title(f"Trying to connect to {text} ...")
                print(f"Trying to connect to {text} ...")
                try:
                    self.tcp_socket.connect(tuple(self.server_ip))
                    self.connected = True
                    print("Connected!")
                    master.destroy()
                    self.message("ROOT", "Connected!")
                    self.start()
                except BaseException as error:
                    print(error)
                    master.title(f"Failed to connect to {text}. Please try again")
                    raise ValueError from error
            master.destroy()
        except ValueError as error:
            print(error)

    def quit(self):
        "Quit the chat"
        print("Thank you for going the chat!")
        self.window.destroy()
        if self.connected:
            self.tcp_socket.close()

    def message(self, username, text):
        "Add a message"
        # Disable to enable editing
        self.main_window.configure(state="normal")

        print(f"{username}: {text}")

        # Change text window
        self.main_window.insert(f"{self.counter}.0", f"{username}: {text}\n")

        length = text.split("\n")
        self.counter += len(length)

        # Enable to disable editing
        self.main_window.configure(state="disabled")

    def chat_server(self):
        "Redirect to listen()"
        self.listen()

    def listen(self):
        "Start listening button"
        start_button = tk.Button(text="Start listening", command=self.start_listen)
        start_button.pack()
        self.start()

    def start_listen(self):
        "Start the listening"
        self.tcp_socket.listen()
        self.message("ROOT", f"Received connection from {self.tcp_socket.return_addr}")
     
    def update(self):
        "Update the window"
        received = self.tcp_socket.recv()
        print(f"Got {received}")
        received = received.decode()
        self.message("PEER", received)
    

    def chat_client(self):
        "Redirect to get_server()"
        self.get_server()

    
    def send(self):
        "Send a message"
        entry = self.entry_window.get("1.0", tk.END)
        # Send code
        self.tcp_socket.send(entry.encode())
        print(f"Sent message: {entry}")

        # Show in main window
        self.message("user", entry)
        # Clear window
        self.entry_window.delete("1.0", tk.END)
 
    def start(self):
        "Packs/running widgets/frames"
        self.entry_window.pack(side=tk.BOTTOM)
        self.exit_button.pack(side=tk.LEFT)
        self.main_window.pack(side=tk.TOP)
        self.submit_button.pack(side=tk.RIGHT)
        self.refresh_button.pack(side=tk.LEFT)
        self.frame.pack()
        self.window.mainloop()

try:
    if sys.argv[1] == "client":
        print("You are in CLIENT mode")
        a = ClientSocket()
        b = Chat(a)
    elif sys.argv[1] == "server":
        print("You are in SERVER mode")
        a = ServerSocket()
        b = Chat(a)
except IndexError as error:
    print(error)
