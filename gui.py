'''
The GUI builder for the chat
'''

# Imports
from tkinter.ttk import Entry
from base_socket import BaseSocket, ClientSocket, ServerSocket, SERVER_PORT
import tkinter as tk
import sys
import time
from ipaddress import ip_address

# The main Chat class
class Chat:
    def __init__(self, tcp_socket) -> None:
        "Initialize the Chat"

        # Sees if it is a subclass of BaseSocket
        if not issubclass(type(tcp_socket), BaseSocket):
            raise AttributeError("Error: Please make sure to use ClientSocket or ServerSocket for the tcp_socket")
        
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
        self.main_window.configure(state="disabled")


        # Starts the correct options
        if isinstance(self.tcp_socket, ClientSocket):
            self.chat_client()
        else:
            self.chat_server()

    def get_server(self):
        "Asks for the server"
        # Starting the window
        print("Entered get_server")
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

        print("Mainloop")
        server_tk.mainloop()
        
    def server_ent_quit(self, master, ent=None) -> None:
        print("Entered server_ent_quit")
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
                except BaseException as e:
                    print(e)
                    master.title(f"Failed to connect to {text}. Please try again")
                    raise ValueError
            master.destroy()
        except BaseException as e:
            print(e)
        print("exited server_ent_quit")
        self.start()

    def quit(self):
        print("Thank you for going the chat!")
        self.window.destroy()
        if self.connected:
            self.tcp_socket.close()

    def push(self, user, text):
        # Disable to enable editing
        self.main_window.configure(state="normal")

        # Change text window

        # Enable to disable editing
        self.main_window.configure(state="disabled")

    def chat_server(self):
        self.tcp_socket.listen()

    def chat_client(self):
        self.get_server()

    
    def send(self):
        entry = self.entry_window.get("1.0", tk.END)
        # Send code
        self.tcp_socket.send(entry.encode())
        # Show in main window
        self.push("user", entry)
        # Clear window
        self.entry_window.delete("1.0", tk.END)
        
    def start(self):
        print("entered start")
        # Packs/running widgets/frames
        self.entry_window.pack(side=tk.BOTTOM)
        self.exit_button.pack(side=tk.LEFT)
        self.main_window.pack(side=tk.TOP)
        self.submit_button.pack(side=tk.RIGHT)
        self.frame.pack()
        self.window.mainloop()

try:
    if sys.argv[1] == "client":
        a = ClientSocket()
        b = Chat(a)
    elif sys.argv[1] == "server":
        a = ServerSocket()
        b = Chat(a)
except BaseException as e:
    print(e)
