import mechanical_mustaches as mm
from mechanical_mustaches import m
import mechanical_mustaches.web.picoweb as picoweb
import mechanical_mustaches.web.ulogging as logging
import json
import esp32
import uasyncio
import agents.stache_board

m.find_outputs()
m.make_rez()

def send_css():
    with open('/mechanical_mustaches/web/static/mustache.css', 'r') as f:
        return f.read().replace('\r\n', '')

def create_webpage():
    page = [f"<html><head><title>Mo's Mayhem</title><style>{send_css()}</style>",
"""
<script>
var source = new EventSource("stacheboard/events");
source.onmessage = function(event) {
  var load = JSON.parse(event.data);
  console.log(load);
  document.getElementById("temp").innerHTML = load.temp;
  document.getElementById("count").innerHTML = load.count;
  document.getElementById("m_state").innerHTML = load.m_state;
""",
    ''.join([f'document.getElementById("{name}").innerHTML = load.{name};' for name, _ in m.the_rez]),
    """}
    source.onerror = function(error) {
        console.log(error);
        document.getElementById("result").innerHTML += "EventSource error:" + error + "<br>";
    }
</script></head><body><br>
<h1>Mo's Stache'board<br></h1><h3>dashboard</h3><strong>
    Count: <div class="stch_brd" id="count"></div>
    M.state: <div class="stch_brd" id="m_state"></div>
    Temp: <div class="stch_brd" id="temp"></div>""",
    ''.join([f'{name.replace("_", ".")}: <div class="stch_brd" id="{name}"></div>' for name, _ in m.the_rez]),
    '<br><br></strong><p>']
    return ''.join(page)

page = create_webpage()

form_data = None

funcs = {
    'disabled': lambda: m.change_state('disabled'),
    'auto': lambda: m.change_state('auto'),
    'teleop': lambda: m.change_state('teleop'),
    'test': lambda: m.change_state('test')
    }


def button(func, color, location):
    return f'<a href="/stacheboard?button_{location}={func}"><button class="button {color}">{func}</button></a>'

def process(form):
    for k, v in form.items():
        if k =='button_m':
            funcs[v]()
        if k =='button_stache':
            agents.stache_board.buttons[v]()

# @site.route("/")
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else: # must be GET
        req.parse_qs()
    print('printing form data', req.form)
    process(req.form)
    yield from picoweb.start_response(resp)
    yield from resp.awrite(page)
    for func in funcs:
        yield from resp.awrite(button(func, 'pink', 'm'))
    yield from resp.awrite('<br><hr><strong>agents.stache_board.buttons</strong><br>')
    for butt in agents.stache_board.buttons:
        yield from resp.awrite(button(butt, 'grey', 'stache'))
    yield from resp.awrite('</p><br><a href="/"><button class="button pink">home</button></a></html>')
    


def events(req, resp):
    print("Event source connected")
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/event-stream\r\n")
    yield from resp.awrite("\r\n")
    i = 0
    try:
        while True:
            load = {"count": i,
                    "temp": esp32.raw_temperature(),
                    "m_state": m.state}
            load.update(m.rez())
            load = "data: {}\n\n".format(json.dumps(load))
            yield from resp.awrite(load)
            yield from uasyncio.sleep(.5)
            i += 1
    except OSError:
        print("Event source connection closed")
        yield from resp.aclose()




ROUTES = [
    ("/", index),
    ("/events", events),
]

app = picoweb.WebApp(__name__, ROUTES)


