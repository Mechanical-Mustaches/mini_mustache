"""
used with Jerry Joypad
"""
import socket
import asyncio

class UDP_Server:
    def __init__(self, address: str, port: int):
        self.addr = address
        self.port = port
        self.conn = tuple()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.setblocking(False)
        self.s.bind((address, port))

        self.raw = b''



    async def check(self):
        while True:
            try:
                data, addr = self.s.recvfrom(1024)  # buffer size is 1024 bytes
                self.conn = addr
                print(f"received message: {data}, {addr} {utime.ticks_ms()}")
                self.s.sendto('hello', addr)

            except OSError:
                pass

            await asyncio.sleep_ms(0)
