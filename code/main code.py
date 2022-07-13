from machine import Pin,PWM
import utime
from neopixel import NeoPixel
import mustache

pixely = Pin(12, Pin.OUT)
actualylight = NeoPixel(pixely, 1)
actualylight[0] = (0,50,200)
actualylight.write()



wally = mustache.Wheels(name='wally')

func_button = Pin(36, Pin.IN)
# input pin on GPIO36

light = Pin(27, Pin.OUT)

dance_time = 1500
        
while True:
    if func_button.value() == 0:
        light.value(1)
        print("somethin something wooo buttonnn")
        wally.move(400, 400)
        utime.sleep_ms(dance_time)
        wally.move(-400, -400)
        utime.sleep_ms(dance_time)
        wally.move(-400, 400)
        utime.sleep_ms(dance_time)
        wally.move(400, -400)
        utime.sleep_ms(dance_time)
        wally.stop()
        light.value(0)
        

#         utime.sleep_ms(100)
#         light.value(1)
#     utime.sleep_ms(20)
#     light.value(0)
        