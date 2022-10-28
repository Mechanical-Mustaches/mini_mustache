import mechanical_mustaches as mm
from mechanical_mustaches.udp_server import UDP_Server

class Joypad(mm.Agent):
    buttons = {
        'green': 1,
        'red': 2,
        'yellow': 4,
        'blue': 8,
        'start': 16,
        'select': 32,
        'up': 64,
        'down': 128,
        'left': 256,
        'right': 512,
        'l_push': 1024,
        'r_push': 2048
    }

    axises = {
        'LX': 0,
        'LY': 1,
        'RX': 2,
        'RY': 3
    }

    def __init__(self, name: str, port: int = 8122):
        super().__init__(name)
        self.socket = UDP_Server(mm.my_ip, port)
        self.old = []
        self.buts = 0
        self.axes  = []

    def get_but(self, button: str) -> bool:
        return self.buts & self.buttons[button]

    def get_axis(self, axis: str) -> float:
        return self.axes[self.axises[axis]]

    def get_but_event(self, button: str) -> None | bool:
        pass




