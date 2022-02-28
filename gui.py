'''
The GUI builder for the chat
'''

# Imports
from tcp_socket import BaseSocket, ClientSocket
import tkinter as tk
import sys
from ipaddress import ip_address

# The main Chat class
class Chat:
    def __init__(self, tcp_socket) -> None:
        "Initialize the Chat"

        # Sees if it is a subclass of BaseSocket
        if not issubclass(type(tcp_socket), BaseSocket):
            #raise AttributeError("Error: Please make sure to use ClientSocket or ServerSocket for the tcp_socket")
            pass
        self.tcp_socket = tcp_socket
        self.server_ip = ""
        self.window = tk.Tk()
        self.window.title("Chat Room")

        if isinstance(self.tcp_socket, ClientSocket):
            self.chat_client()
        else:
            self.chat_server()

        self.window.mainloop()

    def get_server(self):
        "Asks for the server"
        # Starting the window
        server_tk = tk.Tk()
        server_tk.geometry("400x150")
        server_tk.title("Please enter server IPv4")

        # The widgets
        lbl_message = tk.Label(master=server_tk, text="Enter Server IPv4: ")
        ent_entry = tk.Entry(master=server_tk)
        btn_submit = tk.Button(master=server_tk, text="Submit", command=lambda: self.quit(server_tk, ent_entry))

        # Packing/running them
        lbl_message.pack()
        ent_entry.pack()
        btn_submit.pack()

        server_tk.mainloop()

        print(self.server_ip)

    def quit(self, master, ent=None) -> None:
        if ent:
            text = ent.get()
        try:
            if ent:
                ip_address(text)
                self.server_ip = text
            master.destroy()
        except ValueError:
            master.title("Please enter a VALID IPv4")

    def main_window(self):
        pass

    def chat_server(self):
        pass

    def chat_client(self):
        pass

b = "1"
a = Chat(b)
