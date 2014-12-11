import flask, flask.views
from flask import url_for, request, session, redirect
from jinja2 import environment, FileSystemLoader
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, request
from flask import session, redirect
from flask_oauth import OAuth
import os

app = flask.Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = '234234rfascasascqweqscasefsdvqwefe2323234dvsv'

FACEBOOK_APP_ID = '539244542865228'
FACEBOOK_APP_SECRET = 'efaee0037f9320831895a5e9aa4d1bc6'

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': ('email, ')}
)

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)

@app.route('/', methods=['GET', 'POST'])
def index():
    if not session:
        hadtolog = True
        return redirect('login')
    hadtolog = False
    return flask.render_template('index.html',scheme="dark", hadtolog=hadtolog)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return flask.render_template('login.html',scheme="dark")


@app.route("/facebooklogin")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))

@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)
    
    session['signedin'] = True
    session['facebook_token'] = (resp['access_token'], '')
    data = facebook.get('/me').data
    if 'id' in data and 'name' in data:
        session['facebookId'] = data['id']
        session['firstname'] = data['first_name']
        session['lastname'] = data['last_name']
    return redirect(next_url)


@app.route('/changetheme', methods=['GET', 'POST'])
def change_theme():
    scheme = request.args.get('scheme')
    print scheme
    return flask.render_template('index.html',scheme=scheme)


@app.route('/nextpage', methods=['GET', 'POST'])
def next_page():
    return flask.render_template('nextpage.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port=int(os.environ['PORT']), host='0.0.0.0')

    # port=int(os.environ['PORT']), host='0.0.0.0'