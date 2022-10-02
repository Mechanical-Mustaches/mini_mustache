#
# This is a picoweb example showing how to handle form data.
#
import mechanical_mustaches
import mechanical_mustaches.web.picoweb as picoweb
import time

app = picoweb.WebApp(__name__)

the_runs = ''
the_input = ''

def process(form):
    global the_runs
    global the_input
    the_input = ''
    if 'clear' in form: # button press
        the_runs = ''
    
    if 'code' not in form: # initial pageload probably
        return

    try:
        _return = str(eval(form['code'], globals(), locals())).strip('<>')
        the_runs += f">>> {form['code']}\n{_return}\n"
    
    except SyntaxError:
        try:
            code = form['code'].replace('\r', '')
            exec(compile(code , 'input', 'exec'), globals(), locals())
            the_runs +=  f">>> {code}\n"
        except Exception as e:
            the_runs += f">>> {form['code']}\n{e}\n"
            the_input = form['code']
    
    except Exception as e:
        the_runs += f">>> {form['code']}\n{e}\n"
        the_input = form['code']


@app.route("/")
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        req.parse_qs()
    # print(req.form)
    process(req.form)
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"""
<!DOCTYPE html><html><head><style>{send_css()}</style>{script()}</head><body><h1>Mo's Repl</h1><br><form action='repl' method='POST'>
Terminal:<br>
<form action='/repl' method='POST'>
<textarea name="clear" class="textarea" cols=60 rows={the_runs.count('\n') + 6} >{the_runs}</textarea>
<input id="clear" type="submit" value="clear" class="button pink_s">
</form>
<br><br><br><br>
input: <form action="/repl" method="POST" id="mline">
<textarea class="textarea" name="code" autofocus="autofocus" cols=40 rows=4 OnKeyPress="submitOnEnter();">{the_input}</textarea>
<input id="mline_submit" type="submit" value="run" class="button pink_s">
</form>
remember: python uses 4 spaces as indents, but 2 spaces will work here ;)<br>
shift + enter for newline, enter will run code
""")

    yield from resp.awrite('<br><br><br><a href="/"><button class="button grey">home</button></a><br>')


def send_css():
    with open('/mechanical_mustaches/web/static/mustache.css', 'r') as f:
        return f.read().replace('\r\n', '')
    

def script():
    return """<script>
function submitOnEnter(){
    var x = event.keycode
    console.log(x)
    if(event.which === 13 && !event.shiftKey){
        event.target.form.dispatchEvent(new Event("submit", {cancelable: true}));
        event.preventDefault();
    }
}
</script>"""



# <form action='/repl' method='POST'>single line: <input name='code'/><input type='submit' value='run'></form><br>
