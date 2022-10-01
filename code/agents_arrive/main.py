import mechanical_mustaches as mm
from mechanical_mustaches import m
from robot import *


mm.wifi_connect()

mm.start_web_page()

# webrepl.start()


m.run(Robot())

