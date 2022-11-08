import mechanical_mustaches as mm
from mechanical_mustaches.udp_server import UDP_Server
import struct
from mechanical_mustaches import m


def unpack(pack: bytearray) -> tuple[int, int, int, int, int]:
    return struct.unpack('hhhhH', pack[1:])


class Joypad(mm.Agent):
    buttons = {
        'red': 1,
        'blue': 2,
        'yellow': 4,
        'green': 8,
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

    def __init__(self, name: str, port: int=8122, deadzone: int=0):
        super().__init__(name)
        self.socket = UDP_Server(mm.my_ip, port)
        self.old = (0.0,0.0,0.0,0.0,0)  # (LX, LY, RX, RY, buttons: bytearray)
        self.state = (0.0,0.0,0.0,0.0,0)
        self.idx = 0
        self.deadzone = deadzone

    def read(self, _input: str, deadzone=False) -> bool | float:
        if _input in self.buttons:
            return self.state[4] & self.buttons[_input]
        else: # must be axis
            axis = self.state[self.axises[_input]]
            if deadzone:
                if abs(axis) < self.deadzone:
                    return 0.0
            return axis
        

    def read_event(self, button: str) -> None | bool:
        if button not in self.buttons:
            print('argument must be a button')
            raise ValueError
        
        old = self.old[4] & self.buttons[button]
        new = self.state[4] & self.buttons[button]
        if new != old:
            return bool(new)
        else:
            return None


    def check(self):
        self._update()  # this line must be here
        
    
    def disabledPeriodic(self):
        self._update()
        if self.read_event('red') is True:
            print('red ', self.read_event('red'))
            
    
    def _update(self):
        """update buttons from socket"""
        if self.socket.conn:
            m.ss.fill(4,0,10)
            self.old = self.state
            lx, ly, rx, ry, but = unpack(self.socket.jerry) 
            self.state = (lx/32768, ly/32768, rx/32768, ry/32768, but)
        else:
            m.ss.fill(0,0,0)
            self.state = (0,0,0,0,0)
                
    
    def connected(self):
        if self.socket.conn:
            return True
        else:
            return False
    
    def report(self):
        if not self.connected():
            return 'disconnected'
        return f'LX:{self.state[0]:.2f}, LY:{self.state[1]:.2f}, RX:{self.state[2]:.2f}, RY:{self.state[3]:.2f}, b:{self.state[4]:b}'







