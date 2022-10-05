
import config
config.wifi_connect()

config.ss.fill(0,4,2)
import mechanical_mustaches as mm
from mechanical_mustaches import m
from robot import *


mm.start_web_page()

# webrepl.start()

config.ss.fill(0,0,0)
m.run(Robot())

