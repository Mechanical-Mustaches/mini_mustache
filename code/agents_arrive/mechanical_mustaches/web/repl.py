#
# This is a picoweb example showing how to handle form data.
#
import mechanical_mustaches
import mechanical_mustaches.web.picoweb as picoweb
import time
import gc
app = picoweb.WebApp(__name__)



the_runs = ''
the_input = ''
g_imprtd = False


def process(form):
    global the_runs
    global the_input
    global g_imprtd
    the_input = ''
    if 'clear' in form: # button press
        the_runs = ''
    
    if 'code' not in form: # initial pageload probably
        return
    
    code = form['code']
    try:
        _return = str(eval(code, globals(), locals())).strip('<>')
        the_runs += f">>> {code}\n{_return}\n"
    
    except SyntaxError:
        try:
            code = code.replace('\r', '')
            if not g_imprtd:
                exec(compile('globals().update(locals())' , 'input', 'single'), globals(), locals())
                g_imprtd = True
            # _code = compile(code , '<string>', 'single')
            exec(compile(code , 'input', 'single'), globals(), locals())
            # exec(_code, globals(), locals())
            the_runs +=  f">>> {code}\n"
        except Exception as e:
            the_runs += f">>> {code}\n{e}\n"
            the_input = code
    
    except Exception as e:
        the_runs += f">>> {code}\n{e}\n"
        the_input = code


@app.route("/")
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        req.parse_qs()
    # print(req.form)
    process(req.form)
    gc.collect()
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""
<!DOCTYPE html><html><head><style>{send_css()}</style></head><body><h1>Mo's Repl</h1><br><form action='repl' method='POST'>
Terminal:<br>
<form action='/repl' method='POST'>
<textarea name="clear" class="textarea" cols=60 rows={the_runs.count('\n') + 6} >{the_runs}</textarea>
<input id="clear" type="submit" value="clear" class="button pink_s">
</form>
<br><br><br><br>
input: <form action="/repl" method="POST" id="coder">
<textarea class="textarea" name="code" autofocus="autofocus" cols=40 rows=4" onfocus="var temp_value=this.value; this.value=''; this.value=temp_value">{the_input}</textarea>
<input type="submit" value="run" class="button pink_s">
</form>
remember: python uses 4 spaces as indents, but 2 spaces will work here ;)<br>
shift + enter for newline, enter will run code
""")

    yield from resp.awrite(f'<br><br><br><a href="/"><button class="button grey">home</button></a><br>{script()}</body></html>')
    gc.collect()

def send_css():
    with open('/mechanical_mustaches/web/static/mustache.css', 'r') as f:
        return f.read().replace('\r\n', '')
    

def script():
    return """<script>
document.addEventListener('keydown', (event) => {
if(event.key == "Enter"  && !event.shiftKey) {
  document.getElementById("coder").submit();\
}
  }, false);
</script>"""



