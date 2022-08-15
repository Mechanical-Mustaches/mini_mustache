from machine import Pin
import wheels, neo
import utime
from machine import Pin
import uasyncio as asyncio


A = Pin(17, Pin.IN)
B = Pin(5, Pin.IN)
C = Pin(18, Pin.IN)

timmy = mm.Timer()
archie = mm.Autonomous()
wally = wheels.Wheels(name='wally')
nemo = neo.Neo(name='nemo', pin=15, num_pix=5)
lefty = mm.Servo(name='lefty', pin=21)
righty = mm.Servo(name='righty', pin=19)
utime.sleep_ms(10)


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



