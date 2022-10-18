#
# This is a picoweb example showing how to handle form data.
#
import mechanical_mustaches
import mechanical_mustaches.web.picoweb as picoweb
import time
import gc
import uasyncio
import json



the_runs = ''
the_input = ''
g_imprtd = False
the_output = ''

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


def repl_it(form):
    global the_output
    global g_imprtd
    
    
    code = form['code']
    code = code.replace('```', '&')
    code = code.replace('``', '%')
    code = code.replace('`', '+')
    
    # print('code', code)
    the_output = ''
    try:
        _return = str(eval(code, globals(), locals())).strip('<>')
        the_output += f">>> {code}\n{_return}\n"
    
    except SyntaxError:
        try:
            code = code.replace('\r', '')
            if not g_imprtd:
                exec(compile('globals().update(locals())' , 'input', 'single'), globals(), locals())
                g_imprtd = True
            # _code = compile(code , '<string>', 'single')
            exec(compile(code , 'input', 'single'), globals(), locals())
            # exec(_code, globals(), locals())
            the_output +=  f">>> {code}\n"
        except Exception as e:
            the_output += f">>> {code}\n{e}\n"

    
    except Exception as e:
        the_output += f">>> {code}\n{e}\n"

    # print(the_output)



# @app.route("/")
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
<div>
<table>
<tr><td>count:</td><td id="count"> </td></tr>
</table></div><br>
<div style="width: 50%;display: inline-block;">
<div id="terminal" class="terminal-zone"></div><br>
</div>
<br><br><br><br>

<input: <form method="POST" id="coder">
<textarea class="textarea" id='code' name="code" autofocus="autofocus" cols=40 rows=4 onfocus="var temp_value=this.value; this.value=''; this.value=temp_value">
</textarea>
</form><br>
remember: python uses 4 spaces as indents, but 2 spaces will work here ;)<br>
shift + enter for newline, enter will run code
""")

    yield from resp.awrite(f'<br><br><br><a href="/"><button class="button grey">home</button></a><br>{script()}</body></html>')
    gc.collect()


# @app.route("/input")
def inputs(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        req.parse_qs()
    # print('form', req.form)
    repl_it(req.form)
    gc.collect()
    yield from resp.awrite("HTTP 200 OK")
    



def events(req, resp):
    global the_output
    print("Event source connected")
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/event-stream\r\n")
    yield from resp.awrite("\r\n")
    i = 0
    try:
        while True:
            load = {"count": i}
            if the_output:
                load['code'] = the_output
                the_output = ''
            # print('eventing', load, resp)
            yield from resp.awrite("data: {}\n\n".format(json.dumps(load)))
            yield from uasyncio.sleep(.5)
            i += 1
    except OSError:
        print("Event source connection closed")
        yield from resp.aclose()



def send_css():
    with open('/mechanical_mustaches/web/static/mustache.css', 'r') as f:
        return f.read() # .replace('\r\n', '')
    

def script():
    return """
<script type="text/javascript">



function init(){
  this_history = [];
  var index = 0;
}

function writeLineToChat(line)
        {
            var elm = document.getElementById('terminal');
            if (elm)
            {
                var lineElm = document.createElement('div');
                if (line) {
                    lineElm.innerText = line;
                }
                else
                    lineElm.innerHTML = '&nbsp;';
                elm.appendChild(lineElm);
                elm.scrollTop = elm.scrollHeight;
            }
        }

document.getElementById("coder").addEventListener('keydown', (event) => {
  console.log(event.key);
  var xhttp = new XMLHttpRequest();
  coder = document.getElementById("code")
  if (event.key.toUpperCase() === "ARROWUP") {
                console.log(this_history[0]);
            coder.value = this_history[index];
                index += 1;
  }
  else if (event.key.toUpperCase() === "ARROWDOWN") {
                console.log(this_history[0]);
            coder.value = this_history[index];
                index -= 1;
  }

  else if (event.key == "Enter"  && !event.shiftKey) {
    data = coder.value;
    // writeLineToChat(data)
    this_history.unshift(data)
    coder.value = "";
    console.log(data);
    index = 0;
    xhttp.open("POST", "repl/input", false);
    const the_export = new Object();
    data = data.replace('+', '`')
    data = data.replace('%', '``')
    data = data.replace('&', '```')
    the_export.code = data;
    var jsonExport= JSON.stringify(the_export);
    console.log(jsonExport)
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send("code=" + data);
  }
}, false);

document.getElementById("coder").addEventListener('keyup', (event) => {
  console.log(event.key);
  if (event.key == "Enter"  && !event.shiftKey){
    document.getElementById("code").value = "";
  }
}, false);

var source = new EventSource("repl/events");
source.onmessage = function(event) {
  var load = JSON.parse(event.data);
  // console.log(load);
  document.getElementById("count").innerHTML = load.count;
  if ("code" in load){
    writeLineToChat(load.code);
  }
}

window.addEventListener("load", init, false);
</script>

"""






ROUTES = [
    ("/", index),
    ("/events", events),
    ("/input", inputs)
]

app = picoweb.WebApp(__name__, ROUTES)


