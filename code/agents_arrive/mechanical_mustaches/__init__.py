print('running __init__')
from mechanical_mustaches.motor import Motor
from mechanical_mustaches.servo import Servo
from mechanical_mustaches.agent import Agent, m
from mechanical_mustaches.timer import Timer
from mechanical_mustaches.auto import Auto
from mechanical_mustaches.button import Button
from mechanical_mustaches.knob import Knob
import mechanical_mustaches.wifi as wifi


import network
import utime

my_ip = None

def wifi_connect(*args):
    global my_ip
    if args:
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
        print('my ip adress is: ', my_ip)
    else:
        print('creating access point')
        ap = network.WLAN(network.AP_IF) # create access-point interface
        # print(dir(ap.config))
        ap.config(essid='evezor') # set the SSID of the access point
        ap.active(True)         # activate the interface
        my_ip = ap.ifconfig()[0]
        print('my ip address is: ', my_ip)
    print('doing imports')
    
    