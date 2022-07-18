from machine import Pin,PWM,ADC
import utime
from neopixel import NeoPixel
import mustache
import uasyncio as asyncio
 

# pixely = Pin(14, Pin.OUT)
# actualylight = NeoPixel(pixely, 1)
# actualylight[0] = (0,50,200)
# actualylight.write()

nemo = mustache.Neo(name='nemo', pin=15, num=5)
colors = ((20,0,0), (0,20,0), (0,0,20))

for color in colors:
    nemo.fill(*color)
    utime.sleep(.25)
nemo.fill(0, 0, 0)

wally = mustache.Wheels(name='wally')

#func_button = Pin(36, Pin.IN)
# input pin on GPIO36

A = Pin(17, Pin.IN)
B = Pin(5, Pin.IN)
C = Pin(18, Pin.IN)
D = Pin(13, Pin.IN)

light = Pin(27, Pin.OUT)

dance_time = 1500

# red = nemo.fill(20, 0 ,0)
# green = nemo.fill(0, 20, 0)
# blue = nemo.fil(0, 0, 20)
 
A_knob = ADC(Pin(32), atten=ADC.ATTN_11DB)

def I():
    wally.move(800,800)
    nemo.fill(15, 5, 0)
    
def J():
    wally.move(700, 0)
    nemo.fill(10, 10, 0)

def K():
    wally.move(-600, -600)
    nemo.fill(16, 0, 16)

def L():
    wally.move(0, 700)
    nemo.fill(0, 5, 15)
     
def O():
    wally.stop()
    nemo.fill(0, 10, 10)


def dance(): 
    slow = 500
    fast = 700
    wait = 2000
    wally.move(0, slow)
    utime.sleep_ms(wait)
    wally.move(fast, 0)
    utime.sleep_ms(wait)
    wally.move(slow, 0)
    utime.sleep_ms(wait)
    wally.move(slow, slow)
    utime.sleep_ms(wait)
    wally.move(0, fast)
    utime.sleep_ms(wait)
    wally.stop()
    print('done dancing')
   
   
def flash():
    wait = 1000
    nemo.fill(20, 0, 0)
    utime.sleep_ms(wait)
    nemo.fill(0, 20, 0)
    utime.sleep_ms(wait)
    nemo.fill(0, 0, 20)
    utime.sleep_ms(wait)
    nemo.fill(0,15,10)
    utime.sleep_ms(wait)
    nemo.fill(20, 5, 5)
    print('done flashing')
    
    
def vouge():
    wait = 1500
    fast = 800
    slow = 500
    nemo.fill(15, 5, 5)
    wally.move(slow, slow)
    utime.sleep_ms(wait)
    nemo.fill(20, 0, 0)
    wally.move(fast, 0)
    utime.sleep_ms(wait)
    nemo.fill(20, 4, 0)
    wally.move(fast, fast)
    utime.sleep_ms(wait)
    nemo.fill(15, 10, 0)
    wally.move(slow, 0)
    utime.sleep_ms(wait)
    nemo.fill(0, 15, 0)
    wally.move(0, fast)
    utime.sleep_ms(wait)
    nemo.fill(0, 15, 15)
    wally.move(slow, slow)
    utime.sleep_ms(wait)
    nemo.fill(15, 0, 15)
    wally.stop()
    print("done vougeing")
    
    
while True:
    _in = input('gimme input')
    if _in == 'abc':
        print('we got abc')
          
    if not A.value():
        print("A has been pushed")
        dance()
    if not B.value():
        print("B has been pushed")
        flash()
    if not C.value():
        print("C has been pushed")
        vouge()
    if not D.value():
        print("D has been pushed")
#     speed = int(A_knob.read()/2 -1024)
#     print(speed)
#     wally.move(speed, speed)
        
    
    utime.sleep_ms(100)
    
 