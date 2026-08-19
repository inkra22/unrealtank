import socket
import math

class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.sock.setblocking(False)
       


    def send(self, msg: str):
        data = msg.encode("ascii")
        self.sock.sendto(data, (self.host, self.port))



c = Client("127.0.0.1", 5395)
print("Send messages to server")

while True:
    message = input("> ")
    c.send(message)