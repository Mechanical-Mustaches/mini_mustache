import mechanical_mustaches as mm
import math
from machine import Pin
from neopixel import NeoPixel

class Neo(mm.Agent):
    
    rbow = tuple([int((math.sin(math.pi / 18 * i) * 127 + 128) / 10) for i in range(36)])
    
    def __init__(self, pin, num_pix, name='nemo'):
        super().__init__(name)
        self.name = name
        pixels = Pin(pin, Pin.OUT)
        self.neo = NeoPixel(pixels, num_pix)
        self.num_pix = num_pix
        self.r_idx = 0
        self.state = 'sleeping' #rainbow, 
        
    def fill(self, r, g, b):
        """
        Range is 0 --> 255 for (R,G,B) colors 
        """
        for i in range(self.num_pix):
            self.neo[i] = (r, g, b)
        self.neo.write()
     
            
    def check(self):
        if self.state == 'sleeping':
            self.sleeping()
    
    
    def off(self):
        self.fill(0, 0, 0)
        
    
    def sleeping(self):
        self.rainbow()
    
    
    def rainbow(self):
        for i in range(self.num_pix):
            index = (self.r_idx + i*2) % 36
            self.neo[i] = (self.rbow[index], self.rbow[(index + 12)%36], self.rbow[(index + 24)%36])
        self.neo.write()
        self.r_idx = (self.r_idx + 1) % 36
        
