import socket
import math

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.sock.setblocking(False)
        self.sock.bind((self.host, self.port))


    def run(self):
        while True:
            try:
                data, address = self.sock.recvfrom(1024)
                if data:
                    msg = data.decode("ascii")
                    print(msg)

            except BlockingIOError:
                pass



serv = Server("0.0.0.0", 5395)
print("unreal-tank server running")
serv.run()
