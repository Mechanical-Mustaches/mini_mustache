import network
import webrepl
import mechanical_mustache as mm
from machine import Pin, PWM
import utime
import lan
import uasyncio as asyncio
from machine import reset

wlan = network.WLAN(network.AP_IF) # create access-point interface
print('starting')
wlan.config(essid='mustache', password='8122') # set the SSID of the access point

wlan.active(True)         # activate the interface


# webrepl.start()

# wlan = lan.connect()
my_ip = wlan.ifconfig()[0]
print('myip', my_ip)
server = lan.SimpleServer(my_ip, 8122)


A = Pin(17, Pin.IN)
B = Pin(5, Pin.IN)
C = Pin(18, Pin.IN)

nemo = mm.Neo(pin=15, num_pix=5, name="nemo")
nemo.fill(15, 3, 2)
nemo.off()

wally = mm.Wheels(name='wally')
lefty = mm.Servo(name='lefty', pin=21)
righty = mm.Servo(name='righty', pin=19)
utime.sleep_ms(10)

def stache(numb):
    lefty.set(numb)
    righty.set(-numb)

async def shake(angle, num, delay):
    for i in range(10):
        stache(angle)
        await asyncio.sleep_ms(delay)
        stache(-angle)
        await asyncio.sleep_ms(delay)
    stache(0)
    await asyncio.sleep_ms(delay)
    
async def tilt(angle, delay):
    for i in range(5):
        lefty.set(angle)
        righty.set(angle)
        await asyncio.sleep_ms(delay)
        lefty.set(-angle)
        righty.set(-angle)
        await asyncio.sleep_ms(delay)
    stache(0)   

async def dance():
    await tilt(.4, 200)
    wally.move(-400, 400)
    await asyncio.sleep_ms(3500)
    wally.stop()
    await shake(.2, 20, 100)
    
async def loop():
    while True:
        nemo.chk()
        if not A.value():
            asyncio.create_task(shake(.2, 20, 100))
            await asyncio.sleep_ms(200)
        if not B.value():
            asyncio.create_task(tilt(.45, 300))
            await asyncio.sleep_ms(200)
        if not C.value():
            asyncio.create_task(dance())
            await asyncio.sleep_ms(200)
        await asyncio.sleep_ms(20)


        
def web_page():

    html = """
<html>
    <head>
        <title>Mechanical Mustache</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>html{background-color: #0e1ce3; font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #ff0dba; padding: 2vh;}p{font-size: 3.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: 4px solid black;
  border-radius: 12px; color: white; padding: 10px 40px; text-decoration: none; font-size: 50px; margin: 2px; cursor: pointer;}
  .button2{background-color: #ff0dba;}</style>
    </head>
    <body>
    <h1>Mechanical Mustaches</h1>
    <p><strong>Hi, I'm Mo!!!</strong></p>

    <p>
    <p><a href="/dance"><button class="button button2">dance</button></a></p>
    <p><a href="/tilt"><button class="button button2">tilt</button></a></p>
    <p><a href="/shake"><button class="button button2">shake</button></a></p>
    </p>
    


</html>
"""
    return html


async def handle_socket(reader, writer):
    request = (await reader.read(1024))
    print(request)

    await writer.awrite(
        b'it done')
    # await writer.awrite(web_page())
    await writer.aclose()
    return True

async def handle_client(reader, writer):
    request = (await reader.read(1024)).decode('ascii')
    # print(request)
    end = request.find(' HTTP')
    action = request[4:end]
    print(action)
    
    # process request
    if action == '/shake':
        asyncio.create_task(shake(.2, 20, 100))     
    elif action == '/dance':
        asyncio.create_task(dance())
    elif action == '/tilt':
        asyncio.create_task(tilt(.4, 200))
    else:
        pass
    await writer.awrite(
        b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n')

    await writer.awrite(web_page())
    await writer.aclose()
    return True



async def main():
    asyncio.create_task(asyncio.start_server(handle_client, my_ip, 80))
    asyncio.create_task(loop())
    asyncio.create_task(server.chk())
    asyncio.create_task(server.accept())

    while True:
        await asyncio.sleep(5)


while True:
    asyncio.run(main())


# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setblocking(False)
# s.bind(('10.203.136.51', 8122))
# s.listen(5)
# 
# while True:
#     try:
#         sock, adr = s.accept()
#         print(sock, adr, ' got stuff')
#         sock.send('sdlk')
#     except OSError:
#         pass

    
