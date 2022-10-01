#
# This is a picoweb example showing how to handle form data.
#
import mechanical_mustaches
import mechanical_mustaches.web.picoweb as picoweb
import time

app = picoweb.WebApp(__name__)

the_runs = ''

def run_it(form):
    global the_runs
    if 'clear' in form: # button press
        the_runs = ''
    
    if 'code' not in form: # initial pageload probably
        return

    try:
        
        _return = str(eval(form['code'], globals())).strip('<>')
        print('evaling')
        the_runs += f">>> {form['code']}<br>{_return}<br>"
    
    except SyntaxError:
        print('execing')
        code = form['code'].replace('\r', '')
        exec(compile(code , 'input', 'exec'), globals())
        the_runs +=  f">>> {code}<br>"
    
    except Exception as e:
        the_runs += f">>> {form['code']}<br>{e}<br>"
    

@app.route("/")
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        req.parse_qs()
    print(req.form)
    run_it(req.form)
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""<html><head><style>{send_css()}</style></head><body><h1>Mo's Repl</h1><br><form action='repl' method='POST'>
        {the_runs}<br>
        <a href="/repl?clear"><button>clear</button></a><br>
        <form action='/repl' method='POST'>
        repl: <input name='code' />
        <input type='submit' value='run'></form><br>
        <form action="/repl" method="POST">
        <textarea name="code" cols=40 rows=4></textarea>
        <input type="submit" value="run\nmultiline">
        </form>
        """)
    yield from resp.awrite('<br><br><br><a href="/"><button>home</button></a><br>')


def send_css():
    with open('/mechanical_mustaches/web/static/mustache.css', 'r') as f:
        return f.read()
    
    
