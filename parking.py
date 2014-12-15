import flask, flask.views
from flask import url_for, request, session, redirect
from jinja2 import environment, FileSystemLoader
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin, BaseView, expose
from flask import render_template, request
from flask import session, redirect
from flask_oauth import OAuth
import time
import os

app = flask.Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = '234234rfascasascqweqscasefsdvqwefe2323234dvsv'

FACEBOOK_APP_ID = '539244542865228'
FACEBOOK_APP_SECRET = 'efaee0037f9320831895a5e9aa4d1bc6'

oauth = OAuth()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facebook_id = db.Column(db.String(64), unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    join_date = db.Column(db.String(64))

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
        return redirect('login')
    return flask.render_template('index.html',scheme="dark", facebook_id=session['facebookId'], first_name=session['firstname'], last_name=session['lastname'])


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if session:
        return redirect('/')
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

        if not User.query.filter_by(facebook_id=session['facebookId']).first():
            register = User(facebook_id=session['facebookId'], first_name=session['firstname'],
            last_name=session['lastname'], join_date=time.strftime('%b %d, %H:%S %p'))
            db.session.add(register)
            db.session.commit()
    return redirect(next_url)


class IngAdmin(sqla.ModelView):
    column_display_pk = True
admin = Admin(app)
admin.add_view(IngAdmin(User, db.session))


@app.route('/changetheme', methods=['GET', 'POST'])
def change_theme():
    scheme = request.args.get('scheme')
    print scheme
    return flask.render_template('index.html',scheme=scheme)


@app.route('/googlelogin', methods=['GET', 'POST'])
def google_login():
    email = flask.request.form.get('email')
    name = flask.request.form.get('name')
    return flask.render_template('posttest.html',email=email,name=name)


@app.route('/nextpage', methods=['GET', 'POST'])
def next_page():
    return flask.render_template('nextpage.html')\


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/login')


@app.route('/db/rebuild', methods=['GET', 'POST'])
def db_rebuild():
    db.drop_all()
    db.create_all()
    register = User(facebook_id=123456, first_name='Mang',
    last_name='Kanor', join_date=time.strftime('%b %d, %H:%S %p'))
    db.session.add(register)
    db.session.commit()
    return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run(port=int(os.environ['PORT']), host='0.0.0.0')

    # port=int(os.environ['PORT']), host='0.0.0.0'