from argparse import ArgumentParser
from sanic import Sanic
from sanic.response import html, text
from sanic_jinja2 import SanicJinja2
from random import randint
# https://github.com/davitovmasyan/sanic-project

robots_flag = 'TG22{h3ll0_t0_4ll_7h3_r0b0t5_1n_th4_h4u5_fl4g_l34k5_15_b3s7_l34k}'

app = Sanic(__name__)
app.static('/static', './static')
jinja = SanicJinja2(app)

@app.route('/robots.txt')
async def robots(request):
    pos = randint(0, len(robots_flag)-1)
    return html(f"User-agent: * <!-- {pos} {robots_flag[pos]} --> ")

@app.route('/login', methods=['GET', 'POST'])
@jinja.template('login.html')
async def login(request):
    if request.method == 'GET':
        return {}
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'assev' and password == 'v@n5k3l1gh375gr':
        return html(brutef_flag)
    #request['flash']('Wrong username or password!', 'error') # Needs sanic_session...
    return {'flash_err': 1}

@app.route('/')#, methods=['GET', 'GIVE_FLAG', 'OPTIONS', 'GIVE'])
@app.route('/home')#, methods=['GET', 'GIVE_FLAG', 'OPTIONS', 'GIVE'])
@jinja.template('index.html')
async def home(request):
    #if request.method == 'OPTIONS': # Hack to get OPTIONS to work.... REEEEEEEEEEEEEEEEEE
    #    return html('', headers={'allow':'GET,GIVE_FLAG,OPTIONS'})
    #if request.method == 'GIVE_FLAG':
    #    return html(option_flag)
    return {}


if __name__ == '__main__':
    args = ArgumentParser()
    args.add_argument('-i', type=str, default='0.0.0.0', help='IP to listen on')
    args.add_argument('-p', type=int, default=5000, help='Port to run service on')
    args.add_argument('-d', action='store_true', help='Debug mode?' )
    args = args.parse_args()
    app.run(host=args.i, port=args.p, debug=args.d)
