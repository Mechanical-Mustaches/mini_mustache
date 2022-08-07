import socket
import network
import utime
import uasyncio as asyncio

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    aps = wlan.scan()
    print(aps)
    # wlan.connect('ssid', 'password')
    wlan.connect('mustache')
    
    while not wlan.isconnected():
        print(".", end = "")
        utime.sleep_ms(250)
    print('Connection successful')
    print(wlan.ifconfig())
    return wlan


class SimpleServer:
    def __init__(self, address, port):
        self.addr = address
        self.port = port
        
        self.conns = []
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(False)
        self.s.bind(('192.168.4.1', 8122))
        self.s.listen(5)
     
     
    async def accept(self):
        while True:
            try:
                sock, adr = self.s.accept()
                print('got connection from: ', adr)
                sock.send('Hi, I am Mo!!')
                sock.setblocking(False)
                self.conns.append((sock, adr))
            
            except OSError:
                pass
            
            await asyncio.sleep_ms(10)
        
    async def chk(self):
        while True:            
            if self.conns:
                for i in range(len(self.conns)):
                    con = self.conns[i]
                    try:
                        msg = con[0].recv(100)
                        if msg == b'':
                            print('closing connection')
                            con[0].close()
                            self.conns.pop(i)
                            print(self.conns)
                        else:
                            print(msg, ' msg')
                            con[0].send('got it boss')
                    except OSError:
                        pass
                        
            await asyncio.sleep_ms(0)
                        
                
class SimpleClient:
    def __init__(self, *, host: str, port: int):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        print(self.s.recv(1000))
        self.rts = True
        self.s.setblocking(False)
        self.queue = None

    async def chk(self):
        while True:
            try:
                msg = self.s.recv(1000)
                if msg == b'':
                    self.s.close()
                else:
                    print(msg)
                    self.rts = True
            except OSError:
                pass
            
            if self.rts and self.queue:
                print('sending ', self.queue)
                self.s.send(self.queue)
                self.queue = None
            await asyncio.sleep_ms(0)
        
    def send(self, msg):
        print(self.rts, msg, self.queue)
        self.s.send(msg)
#         if self.rts:
#             self.s.send(msg)
#             self.rts = False
#         else:
#             self.queue = msg
            
