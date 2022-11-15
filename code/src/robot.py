import mechanical_mustaches as mm
from mechanical_mustaches import m
from agents import wheels, neo, joypad, mustache
import config
import uasyncio as asyncio



# timmy = mm.Timer()
# wally = wheels.Wheels(**config.wally)
# nemo = neo.Neo(name='nemo', pin=15, num_pix=5)


driver = joypad.Joypad('driver', deadzone=.15)
stache = mustache.Mustache(driver, **config.mustache)
timmy = mm.Timer()
wally = wheels.Wheels(driver, **config.wally)
nemo = neo.Neo(name='nemo', pin=15, num_pix=5)

twirl = [
lambda: stache.wiggle(.5),
lambda: nemo.fill(10,0,0),
lambda: wally.drive(0, -.5),
lambda: timmy.wait(.2),
lambda: stache.wiggle(-.5),
lambda: nemo.fill(0,10,0),
lambda: timmy.wait(.2),
lambda: stache.wiggle(.5),
lambda: nemo.fill(10,0,4),
lambda: timmy.wait(.2),
lambda: stache.wiggle(-.5),
lambda: nemo.fill(0,0,10),
lambda: timmy.wait(.2),
lambda: stache.wiggle(.5),
lambda: nemo.fill(4,0,10),
lambda: timmy.wait(.2),
lambda: stache.wiggle(-.5),
lambda: nemo.fill(10,4,0),
lambda: timmy.wait(.2),
lambda: stache.wiggle(.5),
lambda: nemo.fill(10,0,0),
lambda: timmy.wait(.2),
lambda: stache.wiggle(-.5),
lambda: nemo.fill(0,10,0),
lambda: timmy.wait(.2),
lambda: stache.wiggle(.5),
lambda: nemo.fill(10,0,4),
lambda: timmy.wait(.2),
lambda: stache.wiggle(-.5),
lambda: nemo.fill(0,0,10),
lambda: wally.drive(0, .5),
lambda: timmy.wait(.2),
lambda: stache.twist(-.5),
lambda: nemo.fill(4,0,10),
lambda: timmy.wait(.2),
lambda: stache.twist(.5),
lambda: nemo.fill(10,4,0),
lambda: timmy.wait(.2),
lambda: stache.twist(-.5),
lambda: nemo.fill(10,0,0),
lambda: timmy.wait(.2),
lambda: stache.twist(.5),
lambda: nemo.fill(0,10,0),
lambda: timmy.wait(.2),
lambda: stache.twist(-.5),
lambda: nemo.fill(10,0,4),
lambda: timmy.wait(.2),
lambda: stache.twist(.5),
lambda: nemo.fill(0,0,10),
lambda: timmy.wait(.2),
lambda: stache.twist(-.5),
lambda: nemo.fill(4,0,10),
lambda: timmy.wait(.2),
lambda: stache.twist(.5),
lambda: nemo.fill(10,4,0),
lambda: timmy.wait(.2),
lambda: stache.twist(-.5),
lambda: nemo.fill(10,0,0),
lambda: timmy.wait(.2),
lambda: stache.twist(.5),
lambda: nemo.fill(10,0,4),
lambda: timmy.wait(.2),
lambda: stache.twist(-.5),
lambda: nemo.fill(0,0,10),
lambda: timmy.wait(.2),
lambda: stache.twist(.5),
lambda: nemo.fill(4,0,10),
lambda: timmy.wait(.2),
lambda: stache.twist(0),
lambda: wally.stop()
]

class Robot:
    def __init__(self):
        pass
    
    # AUTO ------------------------------------------------
    
    def autonomousInit(self):
        # m.add_auto(wiggles, name='mr_wiggles')
        pass
    
    
    async def autonomousPeriodic(self):
        await m.auto_check()
    
    # TELEOP ----------------------------------------------
    
    def teleopInit(self):
        nemo.knightride()
    
    
    async def teleopPeriodic(self):
        await m.check()
        
    # ROBOT -----------------------------------------------
    
    def robotInit(self):
        pass
    
    
    async def robotPeriodic(self):
        pass
    
    # TEST ------------------------------------------------
    
    def testInit(self):
        nemo.sleep()
#        pass
    
    
    async def testPeriodic(self):
        pass
    
    # DISABLED --------------------------------------------
    
    def disabledInit(self):
        nemo.rainbow()
#       pass
    
    
    async def disabledPeriodic(self):
        await m.disabledPeriodic() 
        nemo.check()
        if driver.connected():            
            if driver.read_event('red') is True:
                m.run_auto(twirl)
            else:
                wally.check()
                stache.wiggle(-driver.read('RY'))
        
#         pass
        


        
        
        
