
import config
config.wifi_connect()

config.ss.fill(0,4,2)
import mechanical_mustaches as mm
from mechanical_mustaches import m



mm.start_web_page()
import sys
# webrepl.start()
try:
    from robot import *
    config.ss.fill(0,0,0)
    m.run(Robot())
except Exception as e:
    print('failed import', e)
    sys.print_exception(e)
    config.ss.fill(5,0,0)
    import uasyncio
    loop = uasyncio.get_event_loop()
    loop.run_forever()
    


