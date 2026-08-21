import socket
import math

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.sock.setblocking(False)
        self.sock.bind((self.host, self.port))
        self.players = {}

    def handleJOIN(self, addr, text):
        splittedtext = text.split(" ")
        name = splittedtext[1]
        self.players[addr] = name
        print(f"{name} joined from {addr}")
        print(self.players)

        msg = "WELCUM"
        binarymsg = msg.encode("ascii")
        self.sock.sendto(binarymsg, addr)

    def handleCHAT(self, addr, text):
        sentence = text[5:]
        sender = self.players[addr]
        print(f"chat sender is {sender}")
        msg = "CHAT " + sender + ": " + sentence
        binarymsg = msg.encode("ascii")
        print(f"sending to {self.players}")
        for ad in self.players.keys():
            print(f"sending to {ad}")
            self.sock.sendto(binarymsg, ad)


    def run(self):
        while True:
            try:
                data, address = self.sock.recvfrom(1024)
                if data:
                    text = data.decode("ascii")
                    if text.startswith("JOIN"):
                        self.handleJOIN(address, text)

                    if text.startswith("CHAT"):
                        self.handleCHAT(address, text)

                    print(text)

            except BlockingIOError:
                pass



serv = Server("0.0.0.0", 5395)
print("unreal-tank server running")
serv.run()
