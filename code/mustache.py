from machine import Pin,PWM
import utime
from neopixel import NeoPixel
import uasyncio as asyncio

# rangE IS # 0 - 225(RGB) # 

    
class Neo:
    
    colors = [(100,0,0), (85,15,0), (60,40,0), (0,100,0), (0,0,100), (50,0,50)]
    
    def __init__(self, pin, num, name):
        self.name = name
        pixels = Pin(pin, Pin.OUT)
        self.neo = NeoPixel(pixels, num)
        self.num = num
        
    def fill(self, r, g, b):
        """
        Range is 0 --> 255 for (R,G,B) colors 
        """
        for i in range(self.num):
            self.neo[i] = (r, g, b)
        self.neo.write()
     
     #the c in cshow stands for color so its like color show but thats wayyyy too long to type everytime so i made it short
    def cshow(self):
        for color in colors:
            nemo.fill(*color)
            utime.sleep_ms(200)
            
    def chk(self):
        while True:
            for color in self.colors:
                self.fill(*color)


class Motor:
    def __init__(self, f_pin, r_pin, freq, name):
        
        self.name = name
        self.f_pin = f_pin
        self.r_pin = r_pin
        self.freq = freq
        self.f = PWM(Pin(f_pin), freq=freq)
        self.r = PWM(Pin(r_pin), freq=freq)
                 
        utime.sleep_ms(10)
        self.f.duty(0)
        self.r.duty(0)
        
        print("{} has entered the arena".format(self.name))
         
    def intro(self):
        print("My name is {}, my forward pin is {}, my reverse pin is {}, and my frequency is {}. Also mint chocolate chip is the best ice cream flavor.".format(self.name, self.f_pin, self.r_pin, self.freq))

    # + Speed move forward
    # - Speed move backward
    def set(self, speed):
        """
        Range is -1023 <---> 1023 for Speed
        """
        if speed > 0:
            self.f.duty(speed)  # forward pin
            self.r.duty(0)  # reverse pin
        elif speed < 0:
            self.f.duty(0)
            self.r.duty(abs(speed))
        else:
            self.f.duty(0)
            self.r.duty(0)

    def set_raw(self, speed):
        """
        Range is -1023 <---> 1023 for Speed
        """
        if speed > 0:
            self.f.duty(speed)  # forward pin
            self.r.duty(0)  # reverse pin
        elif speed < 0:
            self.f.duty(0)
            self.r.duty(abs(speed))
        else:
            self.f.duty(0)
            self.r.duty(0)


class Wheels:
    def __init__(self, name):
        
        self.name = name
        self.louie = Motor(f_pin=12, r_pin=26, freq=20000, name='louie')
        self.roger = Motor(f_pin=25, r_pin=33, freq=20000, name='roger')

        print("{} has rolledddddddd on in".format(self.name))   

    def move(self, left, right):
        
        self.louie.set(left)
        self.roger.set(right)
        
    def stop(self):
        
        self.louie.set(0)
        self.roger.set(0)
        
        
    
    
        