'''
The GUI builder for the chat
'''

# Imports
from tkinter.ttk import Entry
from base_socket import BaseSocket, ClientSocket, ServerSocket, SERVER_PORT
import tkinter as tk
import sys
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
        btn_submit = tk.Button(master=server_tk, text="Submit", command=lambda: self.server_ent_quit(server_tk, ent_entry))

        # Packing/running them
        lbl_message.pack()
        ent_entry.pack()
        btn_submit.pack()

        server_tk.mainloop()
        
        self.tcp_socket.connect()

    def server_ent_quit(self, master, ent=None) -> None:
        if ent:
            text = ent.get()
        try:
            if ent:
                ip_address(text)
                self.server_ip[0] = text
            master.destroy()
        except ValueError:
            master.title("Please enter a VALID IPv4")

    def quit(self):
        print("Thank you for going the chat!")
        self.window.destroy()
        if self.connected:
            self.tcp_socket.close()

    def push(self):
        pass

    def chat_server(self):
        self.tcp_socket.listen()

    def chat_client(self):
        #self.get_server()
        self.start()
        
    def start(self):

        # Packs/running widgets/frames
        self.entry_window.pack(side=tk.BOTTOM)
        self.exit_button.pack(side=tk.LEFT)
        self.main_window.pack(side=tk.TOP)
        self.frame.pack()
        self.window.mainloop()

b = ClientSocket()
a = Chat(b)
