import mechanical_mustaches as mm
from mechanical_mustaches import m
from machine import Pin, ADC
import wheels, neo
import config
import uasyncio as asyncio

timmy = mm.Timer()
# archie = mm.Auto()
wally = wheels.Wheels(**config.wally)
nemo = neo.Neo(name='nemo', pin=15, num_pix=5)
lefty = mm.Servo(pin=config.port_A['C'], name='lefty')
righty = mm.Servo(pin=config.port_A['D'], name='righty')

A = mm.Button(17)
B = mm.Button(5)
C = mm.Button(18)
D = mm.Button(config.port_B['D'])

knob = mm.Knob(config.port_C['A'])

wiggles = [
    lambda: lefty.set(.8),
    lambda: righty.set(.8),
    lambda: timmy.reset(),
    lambda: timmy.read() > 2,
    lambda: lefty.set(-0.7),
    lambda: righty.set(-0.7),
    lambda: timmy.reset(),
    lambda: timmy.read() > 4,
    lambda: lefty.set(0),
    lambda: righty.set(0),
    lambda: m.retire('mr_wiggles'),
    lambda: m.change_state('disabled')
    ]






class Robot:
    def __init__(self):
        pass
    
    
    def autonomousInit(self):
        m.add_auto(wiggles, name='mr_wiggles')
        # pass
    
    
    async def autonomousPeriodic(self):
        await m.auto_check()
    
    
    def robotInit(self):
        pass
    
    
    async def robotPeriodic(self):
        pass
    
    
    def testInit(self):
        pass
    
    
    async def testPeriodic(self):
        await m.test()

        
    
    def teleopInit(self):
       
        pass
    
    
    async def teleopPeriodic(self):
        await m.check()
        lefty.set(knob.read())
        righty.set(knob.read())
        
        
    def disabledInit(self):
        pass
    
    
    async def disabledPeriodic(self):
        pass    
        if A.read():
            m.change_state('auto')

        
        
        