import socket
import math
import pygame
from player import *
from constants import *


class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.sock.setblocking(False)
        self.clock = pygame.time.Clock()
        self.players = {}
        self.id = None
       


    def send(self, msg: str):
        data = msg.encode("ascii")
        self.sock.sendto(data, (self.host, self.port))

    def handleWELCOME(self, addr, text):
        self.players[1] = Player(1, self.name)
        print("I have been accustomed")

    def handleCHAT(self, addr, text):
        print(text)

    def handleSTATUS(self, addr, text):
        splits = text.split(" ")
        x = int(splits[1])
        y = int(splits[2])
        self.players[1].x = x
        self.players[1].y = y


    

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        while True:

       

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            try:
                #data, address = self.sock.recvfrom(1024)
                data = ''
                address = ''
                if data:
                    text = data.decode("ascii")
                    
                    if text.startswith("WELCUM"):
                        self.handleWELCOME(address, text)

                    if text.startswith("CHAT"):
                        self.handleCHAT(address, text)

                    
                    if text.startsWith("STATUS"):
                        self.handleSATUS(address, text)
                
            except BlockingIOError:
                pass

            keys = pygame.key.get_pressed()

            self.screen.fill("black")

            for p in self.players.values():
                p.render(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)   

                


c = Client("127.0.0.1", 5395)

name=str(input("what is your name?\n"))
c.name = name
c.send("JOIN " + name)
c.run()
