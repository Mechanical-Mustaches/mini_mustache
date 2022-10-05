import config

ss = config.stache_station
from machine import Pin
from neopixel import NeoPixel
import uasyncio as asyncio


class LCD:
    def __init__(self, lcd_sda, lcd_scl):
        import mechanical_mustaches.ssd1306 as ssd1306
        self.i2c = SoftI2C(scl=Pin(lcd_scl), sda=Pin(lcd_sda), freq=400000)
        self.lcd = ssd1306.SSD1306_I2C(width=128, height=64, i2c=i2c, addr=0x3c, external_vcc=False)

    def print(self, line):
        print(line)
    
    def clear(self):
        self.lcd.fill(0)
        self.lcd.show()


class StacheStation:
    def __init__(self, hbt_led, function_button, neo_status, **kwargs):
        self.hbt_led = Pin(hbt_led, Pin.OUT)
        self.function_button = Pin(function_button, Pin.IN)
        self.neo = NeoPixel(Pin(neo_status, Pin.OUT), 1)
        self.neo[0] = (0,0,0)
        self.neo.write()


    def check(self):
        if not self.function_button.value():
            print('function button pressed')
            self.neo[0] = (4,12,0)
            self.neo.write()
            raise KeyboardInterrupt
        
    async def hbt(self):
        while True:
            self.hbt_led.value(not self.hbt_led.value())
            await asyncio.sleep_ms(500)
        
    def fill(self, r, g, b):
        self.neo[0] = (r,g,b)
        self.neo.write()
        
    
        

    