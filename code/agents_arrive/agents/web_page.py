import mechanical_mustaches as mm
import mechanical_mustaches.web.picoweb as picoweb
import mechanical_mustaches.web.ulogging as logging
logging.basicConfig(level=logging.INFO)

site = picoweb.WebApp(__name__)




def web_page():

    html = """
<html>
    <head>
        <title>Mo's Mayhem</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}.button3{background-color: #06876f;}.button4{background-color: #eb3440;}</style>
    </head>
    <body>
    <h1>Evezor Web Interface</h1>
    <p>
    <a href="/camera"><button class="button button2">dance</button></a><br>
    <a href="/form"><button class="button">teleop</button></a><br>

    </p>
</html>
"""
    return html



@site.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(web_page())
    
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

