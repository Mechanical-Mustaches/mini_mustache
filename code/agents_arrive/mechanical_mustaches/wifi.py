import network
import utime

my_ip = None

def connect(*args):
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



# import machine
# id =machine.unique_id()
# print(id)
# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# 
# 
# for letter in id:
#     print(type(letter))
#     print(byteletter, end=' ')
#     if letter.encode('utf8') in letters:
#         print(letter)
#     else:
#         print('m')
