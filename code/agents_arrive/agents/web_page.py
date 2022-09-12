import mechanical_mustaches as mm
from mechanical_mustaches import m
import mechanical_mustaches.web.picoweb as picoweb
import mechanical_mustaches.web.ulogging as logging
logging.basicConfig(level=logging.INFO)

site = picoweb.WebApp(__name__)

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
  .button2{background-color: #ff0dba;}.button3{background-color: #06876f;}.button4{background-color: #eb3440;}</style>
    </head>
    <body>
    <h1>Mo's Mayhem</h1>
    <p>""")
    for func in funcs:
        yield from resp.awrite(button(func))
    yield from resp.awrite('</p></html>')
    
@site.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(web_page())

@site.route("/exit")
def exit(req, resp):
    print('exiting')
    raise KeyboardInterrupt
print('loading run')
site.run(debug=1, port=80, host=mm.my_ip)

