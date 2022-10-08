
import config
config.wifi_connect()


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
    sys.print_exception(e)
    with open('/mechanical_mustaches/web/errors.log', 'w') as f:
        sys.print_exception(e, f)
    config.ss.fill(5,0,0)
    print("BOOT COMPLETE")
    import uasyncio
    loop = uasyncio.get_event_loop()
    loop.run_forever()
    


