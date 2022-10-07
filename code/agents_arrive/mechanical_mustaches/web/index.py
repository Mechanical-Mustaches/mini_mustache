import mechanical_mustaches as mm
from mechanical_mustaches import m
import mechanical_mustaches.web.picoweb as picoweb
import mechanical_mustaches.web.ulogging as logging
import json
import esp32
import uasyncio
import agents.stache_board
import config
logging.basicConfig(level=logging.INFO)

import mechanical_mustaches.web.repl as repl
import mechanical_mustaches.web.stacheboard as stacheboard
import mechanical_mustaches.web.editor as editor

site = picoweb.WebApp(__name__)


@site.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""
<!DOCTYPE html><html><head><title>Mo's Mayhem</title><style>{send_css()}</style></head><body>
<h1 style="font-size:40px">Mo</h1><p style="font-size:20px; color: #FFFFFF;">by: The Mechanical Mustaches</p>
<img src='mechanical_mustaches/web/static/mm_logo.png'style="width: 150px;"></img><br>
<img src='mechanical_mustaches/web/static/FIRST_Horz_RGB.png' style="width: 150px;" /></img><br></body><html><br>
FIRST® Robotics Team 8122<br>
<a href="/repl"><button class="button grey">repl</button></a>
<a href="/stacheboard"><button class="button grey">stacheboard</button></a>
<a href="/editor"><button class="button grey">editor</button></a>
<a href="/about"><button class="button grey">about</button></a><br><br><br>
<p style="font-size:8px">FIRST ® , the FIRST® logo, FIRST ® Robotics Competition, and FIRST ® Tech Challenge, are registered
trademarks of FIRST ® (<a href="http://www.firstinspires.org">www.firstinspires.org</a>) which is not overseeing, involved with, or
responsible for this activity, product, or service.</p></html>
""")


@site.route("/about")
def about(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""
<!DOCTYPE html><html><head><title>about</title><style>{send_css()}</style></head><body>
<h1 style="font-size:40px">Mo</h1><p style="font-size:20px; color: #FFFFFF;">by: The Mechanical Mustaches</p>
<img src='mechanical_mustaches/web/static/mm_logo.png'style="width: 150px;"></img><br>
<img src='mechanical_mustaches/web/static/FIRST_Horz_RGB.png' style="width: 150px;" /></img><br></body><html><br>
FIRST® Robotics Team 8122<br>
<p> write about us here !!!</p>
<a href="/"><button class="button grey">home</button></a>
<p style="font-size:8px">FIRST ® , the FIRST® logo, FIRST ® Robotics Competition, and FIRST ® Tech Challenge, are registered
trademarks of FIRST ® (<a href="http://www.firstinspires.org">www.firstinspires.org</a>) which is not overseeing, involved with, or
responsible for this activity, product, or service.</p></html>
""")


def send_css():
    with open('/mechanical_mustaches/web/static/mustache.css', 'r') as f:
        return f.read().replace('\r\n', '')




site.mount('/repl', repl.app)
site.mount('/editor', editor.app)
site.mount('/stacheboard', stacheboard.app)
site.run(debug=1, port=80, host=config.my_ip)

