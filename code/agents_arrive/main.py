import mechanical_mustaches as mm
from mechanical_mustaches import m
from machine import Pin, ADC
import wheels, neo
import utime
from machine import Pin
import uasyncio as asyncio
import config

knob = mm.Knob(config.port_C['A'])
 
A = mm.Button(17)
B = mm.Button(5)
C = mm.Button(18)
D = mm.Button(config.port_B['D'])

# timmy = mm.Timer()
# archie = mm.Autonomous()
wally = wheels.Wheels(**config.wally)
# nemo = neo.Neo(name='nemo', pin=15, num_pix=5)
lefty = mm.Servo(pin=config.port_A['C'], name='lefty')
righty = mm.Servo(pin=config.port_A['D'], name='righty')
# utime.sleep_ms(10)


# def stache(numb):
#     lefty.set(numb)
#     righty.set(-numb)
# 
# async def shake(angle, num, delay):
#     for i in range(10):
#         stache(angle)
#         await asyncio.sleep_ms(delay)
#         stache(-angle)
#         await asyncio.sleep_ms(delay)
#     stache(0)
#     await asyncio.sleep_ms(delay)
#     
# async def tilt(angle, delay):
#     for i in range(5):
#         lefty.set(angle)
#         righty.set(angle)
#         await asyncio.sleep_ms(delay)
#         lefty.set(-angle)
#         righty.set(-angle)
#         await asyncio.sleep_ms(delay)
#     stache(0)   
# 
# async def dance():
#     await tilt(.4, 200)
#     wally.move(-400, 400)
#     await asyncio.sleep_ms(3500)
#     wally.stop()
#     await shake(.2, 20, 100)


# async def loop():
#     while True:
#         nemo.chk()
#         if not A.value():
#             asyncio.create_task(shake(.2, 20, 100))
#             await asyncio.sleep_ms(200)
#         if not B.value():
#             asyncio.create_task(tilt(.45, 300))
#             await asyncio.sleep_ms(200)
#         if not C.value():
#             asyncio.create_task(dance())
#             await asyncio.sleep_ms(200)
#         await asyncio.sleep_ms(20)



# def test():
#     archie.run(wiggles)
#     while True:
#         archie.check()
#         utime.sleep_ms(0)


# async def main():
#     # asyncio.create_task(asyncio.start_server(handle_client, my_ip, 80))
#     asyncio.create_task(loop())
#     # asyncio.create_task(server.chk())
#     # asyncio.create_task(server.accept())
# 
#     while True:
#         await asyncio.sleep(5)


# while True:
#     asyncio.run(main())

while True:
    lefty.set(knob.read())
    righty.set(knob.read())
    utime.sleep_ms(20)



