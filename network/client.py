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

    def handleWELCOME(self, addr, text):
        print("I have been accustomed")

    def handleCHAT(self, addr, text):
        print(text)

    def run(self):
        while True:
            try:
                data, address = self.sock.recvfrom(1024)
                if data:
                    text = data.decode("ascii")
                    
                    if text.startswith("WELCUM"):
                        self.handleWELCOME(address, text)

                    if text.startswith("CHAT"):
                        self.handleCHAT(address, text)


                    
                
            except BlockingIOError:
                usertext = input("> ")
                self.send("CHAT " + usertext)

                




c = Client("127.0.0.1", 5395)
print("Send messages to server")

name=str(input("what is your name?\n"))
c.send("JOIN " + name)
c.run()
