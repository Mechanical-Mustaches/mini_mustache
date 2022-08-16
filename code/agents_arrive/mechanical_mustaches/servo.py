from machine import Pin, PWM
import utime



class Servo:
    # range is 70 --> 650
    def __init__(self, pin: int, *, freq:int=250, _min:int= 70, _max:int= 650, name='servo'):
        self.name = name
        self.pin = PWM(Pin(pin), freq=freq)
        self.min = _min
        self.max = _max
        
        utime.sleep_ms(10)
        self.pin.duty(0)
        
        
    def raw(self, duty):
        self.pin.duty(duty)
        
    def set(self, pos):
        """ we want range from -1 to 1 """ 
        duty = self.clamp(pos, -1, 1)
        self.pin.duty(duty)
    
    def degrees(self, deg):
        """ input deg from 0 to 180 """
        duty = self.clamp(deg , 0, 180)
        self.pin.duty(duty)
    
    def clamp(self, val, _min, _max):
        return int(((val - _min) / (_max - _min)) * (self.max - self.min) + self.min)
    
