import mechanical_mustaches as mm
from mechanical_mustaches import m
import wifi_cfg


# Start WIFI
# mm.wifi_connect(*wifi_cfg.cfg)  # comment to disable wifi    
mm.wifi_connect()

# mm.start_web_page()  # comment to disable webpage  

# webrepl.start()  # comment to diable webrepl (this is NOT the repl page on the website)

mm.boot(initial_state = 'disabled')
from robot import *


  #----------------------------------
  #  comment all code above and write code in scratchpad
  #  for quick to boot code
  #----------------------------------
  

# from scratchpad import *  # uncomment to use scratchpad
