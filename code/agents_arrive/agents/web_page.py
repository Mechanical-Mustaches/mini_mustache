import mechanical_mustaches as mm
from mechanical_mustaches import m
import mechanical_mustaches.web.picoweb as picoweb
import mechanical_mustaches.web.ulogging as logging
import json
import esp32
logging.basicConfig(level=logging.INFO)



form_data = None

funcs = {
    'print': lambda: print('A_butt is cool'),
    'ink': lambda: print('B_butt is fire'),
    'disabled': lambda: m.change_state('disabled'),
    'auto': lambda: m.change_state('auto'),
    'teleop': lambda: m.change_state('teleop'),
    'test': lambda: m.change_state('test')
    }


def button(func):
    return f'<a href="/?button={func}"><button class="button button2">{func}</button></a>'

def process(form):
    for k, v in form.items():
        if k =='button':
            funcs[v]()

@site.route("/")
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else: # must be GET
        req.parse_qs()
    print('printing form data', req.form)
    process(req.form)
    yield from picoweb.start_response(resp)
    yield from resp.awrite("""
<html>
    <head>
        <title>Mo's Mayhem</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>html{background-color: #0e1ce3; font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #ffffff; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #ff0dba;}.button3{background-color: #06876f;}.button4{background-color: #eb3440;}.myDiv{display: block;margin-left: auto;
  margin-right: auto; width: 300px;
  border: 5px outset #2E8B57; background-color: lightblue; text-align: center;}</style>
  <script>
var source = new EventSource("cnc/events");
source.onmessage = function(event) {
    var load = JSON.parse(event.data);
    console.log(load);
    document.getElementById("temp").innerHTML = load.temp;
    document.getElementById("count").innerHTML = load.count;
}
source.onerror = function(error) {
    console.log(error);
    document.getElementById("result").innerHTML += "EventSource error:" + error + "<br>";
}
</script>
    </head>
    <body>
    <h1>Mo's Mayhem</h1>
    <h3>machine status: </h3><br>
<strong>
Count: <div class="myDiv" id="count"></div>
Status: <div class="myDiv" id="status"></div>
Position: <div class="myDiv" id="position"></div>
Temp: <div class="myDiv" id="temp"></div></strong>
<br>
<br>
    <p>""")
    for func in funcs:
        yield from resp.awrite(button(func))
    yield from resp.awrite('</p></html>')
    
    
    

def events(req, resp):
    print("Event source connected")
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/event-stream\r\n")
    yield from resp.awrite("\r\n")
    i = 0
    try:
        while True:
            load = {"count": i,
                    "temp": esp32.raw_temperature()}
            load = "data: {}\n\n".format(json.dumps(load))
            yield from resp.awrite(load)
            yield from uasyncio.sleep(.5)
            i += 1
    except OSError:
        print("Event source connection closed")
        yield from resp.aclose()



site = picoweb.WebApp(__name__, ROUTES)

ROUTES = [
    ("/", index),
    ("/events", events),
]
site.run(debug=1, port=80, host=mm.my_ip)

