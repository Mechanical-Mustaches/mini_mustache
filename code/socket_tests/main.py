my_ip = None

def wifi_connect(*args):

    import network
    import utime
    import machine
    import utime
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
    else:
        letters = "ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
        id = list(machine.unique_id())
        ap_name = 'mustache-' + ''.join([letters[l % len(letters)] for l in id])
        print('creating access point')

        ap = network.WLAN(network.AP_IF) # create access-point interface
        # print(dir(ap.config))
        utime.sleep_ms(500)
        ap.config(essid=ap_name) # set the SSID of the access point
        utime.sleep_ms(500)
        ap.active(True)         # activate the interface
        my_ip = ap.ifconfig()[0]


wifi_connect()
print(my_ip)

from ws_connection import ClientClosedError
from ws_server import WebSocketServer, WebSocketClient


class TestClient(WebSocketClient):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        try:
            msg = self.connection.read()
            if not msg:
                return
            print(msg)
            msg = msg.decode("utf-8")
            items = msg.split(" ")
            cmd = items[0]
            if cmd == "Hello":
                self.connection.write(cmd + " World")
                print("Hello World")
        except ClientClosedError:
            self.connection.close()


class TestServer(WebSocketServer):
    def __init__(self):
        super().__init__("test.html", 2)

    def _make_client(self, conn):
        return TestClient(conn)


server = TestServer()
server.start()
try:
    while True:
        server.process_all()
except KeyboardInterrupt:
    pass
server.stop()


