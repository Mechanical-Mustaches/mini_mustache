print('running __init__')
from mechanical_mustaches.motor import Motor
from mechanical_mustaches.servo import Servo
from mechanical_mustaches.timer import Timer
from mechanical_mustaches.auto import Auto
from mechanical_mustaches.button import Button
from mechanical_mustaches.knob import Knob
from mechanical_mustaches.lcd import LCD
from mechanical_mustaches.agent import Agent

def invite_m():
    globals()['m'] = __import__('mechanical_mustaches.agent', globals(), locals(), [], 0).m
    StacheStation = __import__('mechanical_mustaches.stache_station', globals(), locals(), [], 0).StacheStation

def start_web_page():
    import mechanical_mustaches.web.index

    