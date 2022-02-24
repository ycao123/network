'''
The GUI builder for the chat
'''

from tcp_socket import BaseSocket, ClientSocket
import tkinter as tk
import sys
class Chat:
    def __init__(self, tcp_socket) -> None:
        "Initialize the Chat"

        # Sees if it is a subclass of BaseSocket
        if not issubclass(type(tcp_socket), BaseSocket):
            #raise AttributeError("Error: Please make sure to use ClientSocket or ServerSocket for the tcp_socket")
            pass
        self.tcp_socket = tcp_socket
        self.window = tk.Tk()
        self.window.mainloop()
        self.get_server()


        if isinstance(self.tcp_socket, ClientSocket):
            pass
        else:
            pass


    def get_server(self):
        server_tk = tk.Tk()
        message = tk.Label(server_tk, text="Enter Server IP: ", )
        
        message.pack()
        server_tk.mainloop()

b = "1"
a = Chat(b)
