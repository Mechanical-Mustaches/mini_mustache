


wally = {
    'name': 'wally',
    'louie' : {
        'f_pin': 12,
        'r_pin': 26,
        'freq': 20000,
        'name': 'louie',
        'inverted': True
        },
    'roger': {
        'f_pin': 25,
        'r_pin': 33,
        'freq': 20000,
        'name': 'roger',
        'inverted': True
        }
    }

nemo = {
    'name': 'nemo',
    'pin': 15,
    'num_pix': 5
    }

stache_station = {
    'hbt_led': 27,
    'function_button': 36,
    'neo_status': 14,
    'enable': True
    }

port_A = {
    'A' : 23,
    'B': 22,
    'C': 21,
    'D': 19
    }

port_B = {
    'A' : 17,
    'B': 5,
    'C': 18,
    'D': 13
    }

port_C = {
    'A' : 32,
    'B': 35,
    'C': 34,
    'D': 39
    }


with open('/mechanical_mustaches/web/errors.log', 'w') as f:
    f.write('')

import uasyncio as asyncio
from mechanical_mustaches import StacheStation
ss = None
if stache_station['enable']:
    ss = StacheStation(**stache_station)
    loop = asyncio.get_event_loop()
    loop.create_task(ss.hbt())
    


my_ip = None

def wifi_connect(*args):
    import network
    import utime
    import machine
    import utime
    global my_ip
    if args:
        ss.fill(0,4,0)
        _ssid, password = args
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(_ssid, password)
        while not wlan.isconnected():
            utime.sleep(1)
            print('.', end='')
        print('.')
        my_ip = wlan.ifconfig()[0]
    else:
        ss.fill(0,4,0)
        letters = "ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
        id = list(machine.unique_id())
        ap_name = 'mustache-' + ''.join([letters[l % len(letters)] for l in id])
        print('creating access point', ap_name)
        ap = network.WLAN(network.AP_IF) # create access-point interface
        # print(dir(ap.config))
        utime.sleep_ms(500)
        ap.config(essid=ap_name) # set the SSID of the access point
        utime.sleep_ms(500)
        ap.active(True)         # activate the interface
        my_ip = ap.ifconfig()[0]
    ss.fill(0,0,0)
    print('my ip address is: ', my_ip)

ss.fill(0,4,2)