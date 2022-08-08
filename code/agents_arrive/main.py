
import mechanical_mustaches as mm
from mechanical_mustaches import m
from agents import wheels, neo
import utime

print('loading main.py')


wally = wheels.Wheels(name='wally')
nemo = neo.Neo(name='nemo', pin=15, num_pix=5)


while True:
    m.chk()
    utime.sleep_ms(20)
    

