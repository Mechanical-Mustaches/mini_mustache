#
# This is a picoweb example showing how to handle form data.
#
import mechanical_mustaches
import mechanical_mustaches.web.picoweb as picoweb
import time

app = picoweb.WebApp(__name__)


def run_it(form):
    if 'code' not in form:
        return ''

    try:
        _return = str(eval(form['code'])).strip('<>')
    except Exception as e:
        _return = e
    return f'''
>>> {form['code']}<br>
{_return}
'''    

@app.route("/")
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        # Note: parse_qs() is not a coroutine, but a normal function.
        # But you can call it using yield from too.
        req.parse_qs()
    # print(req.form)
    print(mechanical_mustaches.my_ip)
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""<html><head><link rel="stylesheet" href='mechanical_mustaches/web/static/mustache.css'></head><body><h1>Mo's Repl</h1><br><form action='repl' method='POST'>
        repl: <input name='code' />
        <input type='submit' value='enter'></form><br>
        """)
    
    yield from resp.awrite(run_it(req.form))
    yield from resp.awrite('<br><br><br><a href="/"><button>home</button></a><br>')
    yield from resp.awrite(b"<img src='mechanical_mustaches/web/static/mm_logo.png'></img><br>")
    yield from resp.awrite(b"<img src='mechanical_mustaches/web/static/FIRST_Horz_RGB.png'></img><br></body><html>")



