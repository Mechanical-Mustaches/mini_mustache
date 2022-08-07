import esp32
import machine as upython
from machine import Pin, ADC, Timer, PWM, UART, CAN
from neopixel import NeoPixel
import utime
import struct
from utilities import Button, Analog
import lan
import uasyncio as asyncio

print('joypad board')
print('v1.1')
print('initializing')
this_id = 1200
print(this_id)

# Set up standard components
upython.freq(240000000)
hbt_led = Pin(5, Pin.OUT, value=0)

func_button = Pin(36, Pin.IN) # Has external pullup

neo_status_pin = Pin(17, Pin.OUT)
neo_status = NeoPixel(neo_status_pin, 1)
neo_status[0] = (0, 0, 0)
neo_status.write()


neo_bar_pin = Pin(12, Pin.OUT)
neo_bar = NeoPixel(neo_bar_pin, 5)

def set_bar(r,g,b):
    for i in range(5):
        neo_bar[i] = (r, g, b)
    neo_bar.write()

set_bar(0,0,0)


sta = lan.connect()
my_ip = sta.ifconfig()[0]
# api = API(host='10.203.136.51', port=8122, my_ip=my_ip)
sock = lan.SimpleClient(host='192.168.4.1', port=8122)


def send_socket(state, button):
    sock.send(button.name.encode() + struct.pack('B', state))

def sock_analog(stick):
    sock.send('s,{}'.format(stick.state).encode())
green_button = Button('green', 25, True, 50, callback=send_socket)
red_button = Button('red', 33, True, 51, callback=send_socket)
blue_button = Button('blue', 27, True, 52, callback=send_socket)
yellow_button = Button('yellow', 26, True, 53, callback=send_socket)
start_button = Button('start', 13, True, 54, callback=send_socket)
select_button = Button('select', 15, True, 55, callback=send_socket)
up_button = Button('up', 21, True, 56, callback=send_socket)
down_button = Button('down', 23, True, 57, callback=send_socket)
left_button = Button('left', 19, True, 58, callback=send_socket)
right_button = Button('right', 22, True, 59, callback=send_socket)
l_joy_push = Button('l_joy_push', 18, True, 60, callback=send_socket)
r_joy_push = Button('r_joy_push', 14, True, 61, callback=send_socket)

l_joy_x = Analog('L_X', 35, 62, callback=sock_analog)
l_joy_y = Analog('L_Y', 32, 63, callback=sock_analog)
r_joy_x = Analog('R_X', 34, 64, callback=sock_analog)
r_joy_y = Analog('R_Y', 39, 65, callback=sock_analog)


async def loop():
    while True:
        up_button.chk()
        select_button.chk()
        start_button.chk()
        yellow_button.chk()
        blue_button.chk()
        red_button.chk()
        green_button.chk()
        down_button.chk()
        left_button.chk()
        right_button.chk()
        l_joy_push.chk()
        r_joy_push.chk()

        l_joy_y.chk()
        l_joy_x.chk()
        r_joy_y.chk()
        r_joy_x.chk()
        await asyncio.sleep_ms(20)

    
async def main():
    asyncio.create_task(sock.chk())
    asyncio.create_task(loop())

    while True:
        await asyncio.sleep(5)


while True:
    asyncio.run(main())



