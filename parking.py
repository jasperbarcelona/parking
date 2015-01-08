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
from functools import wraps
import time
import os


app = flask.Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = '234234rfascasascqweqscasefsdvqwefe2323234dvsv'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# os.environ['DATABASE_URL']
FACEBOOK_APP_ID = '539244542865228'
FACEBOOK_APP_SECRET = 'efaee0037f9320831895a5e9aa4d1bc6'

oauth = OAuth()

PAGES = [
'feu'
]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    join_date = db.Column(db.String(64))

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    city = db.Column(db.String(64))
    image = db.Column(db.String(64))
    page = db.Column(db.String(64))

class Slot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64))
    destination = db.Column(db.String(64))
    level = db.Column(db.Integer)
    status = db.Column(db.Integer)

class IngAdmin(sqla.ModelView):
    column_display_pk = True
admin = Admin(app)
admin.add_view(IngAdmin(User, db.session))
admin.add_view(IngAdmin(Destination, db.session))
admin.add_view(IngAdmin(Slot, db.session))


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
    session['changed'] = False
    destinations = Destination.query.all()
    return flask.render_template('index.html',scheme="dark", dest=destinations, display_name=session['displayName'], image=session['image'])

# , first_name=session['firstname'], last_name=session['lastname']
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
        session['displayName'] = data['first_name']+' '+data['last_name']
        session['lastname'] = data['last_name']
        session['email'] = data['email']
        session['image'] = 'https://graph.facebook.com/'+data['id']+'/picture?type=large'

        if not User.query.filter_by(email=session['email']).first():
            register = User(display_name=session['displayName'],
            email=session['email'], join_date=time.strftime('%b %d, %H:%S %p'))

            db.session.add(register)
            db.session.commit()
    return redirect(next_url)


@app.route('/changetheme', methods=['GET', 'POST'])
def change_theme():
    scheme = request.args.get('scheme')
    print scheme
    return flask.render_template('index.html',scheme=scheme)


@app.route('/googlelogin', methods=['GET', 'POST'])
def google_login():
    session['email'] = flask.request.form.get('email')
    session['displayName'] = flask.request.form.get('displayName')
    session['image'] = flask.request.form.get('image')
    if not User.query.filter_by(email=session['email']).first():
            register = User(display_name=session['displayName'],
            email=session['email'], join_date=time.strftime('%b %d, %H:%S %p'))

            db.session.add(register)
            db.session.commit()
    return redirect('/')


@app.route('/map', methods=['GET', 'POST'])
def map():
    session['page'] = flask.request.form.get('page')
    if not session['page'] or session['page'] not in PAGES:
        return flask.render_template('notfound.html')
    slots = Slot.query.filter_by(destination=session['page'], level=1).order_by(Slot.id) 
    return flask.render_template(session['page']+'.html', slots=slots)


@app.route('/home', methods=['GET', 'POST'])
def home():
    session['available'] = 0
    destinations = Destination.query.all()
    return flask.render_template('home.html',scheme="dark", dest=destinations)


@app.route('/count', methods=['GET', 'POST'])
def get_count():
    if not session['page'] or session['page'] not in PAGES:
        session['available'] = 0
    session['available'] = Slot.query.filter_by(destination=session['page'], level=1, status=0).count()
    return flask.render_template('available.html', available=session['available'])


@app.route('/refresh', methods=['GET', 'POST'])
def refresh_map():
    if not session['available'] == Slot.query.filter_by(destination=session['page'], level=1, status=0).count():
        slots = Slot.query.filter_by(destination=session['page'], level=1).order_by(Slot.id) 
        session['available'] = Slot.query.filter_by(destination=session['page'], level=1, status=0).count()
        session['changed'] = True
        return flask.render_template(session['page']+'.html', slots=slots)
    return ('',204)


@app.route('/refreshcount', methods=['GET', 'POST'])
def refresh_count():
    if session['changed'] == True:
        return flask.render_template('available.html', available=session['available'])
        session['changed'] = False
    return ('',204)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/login')


@app.route('/update', methods=['GET', 'POST'])
def update_db():
    destination = flask.request.args.get('dest')
    number = flask.request.args.get('num')
    status = flask.request.args.get('status')

    slot_to_update = Slot.query.filter_by(destination=destination, number=number).first()
    slot_to_update.status = status
    db.session.commit()
    return 'Database Updated Successfully'


@app.route('/db/rebuild', methods=['GET', 'POST'])
def db_rebuild():
    db.drop_all()
    db.create_all()
    register = User(display_name='Mang Kanor', email='kanor.mang@gmail.com',
    join_date=time.strftime('%b %d, %H:%S %p'))

    dest = Destination(name="Glorietta", city="Makati City", 
    image="../static/images/glorietta.jpg", page="feu")

    dest1 = Destination(name="Greenbelt", city="Makati City", 
    image="../static/images/greenbelt.jpg", page="greenbelt")

    dest2 = Destination(name="Resorts World Manila", city="Pasay City", 
    image="../static/images/rwb.jpg", page="rwb")

    dest3 = Destination(name="Robinsons Magnolia", city="Quezon City", 
    image="../static/images/magnolia.jpg", page="magnolia")

    dest4 = Destination(name="Robinsons Galeria", city="Quezon City", 
    image="../static/images/gale.jpg", page="gale")

    slot = Slot(number="mkt l-1", destination="feu", level=1, status=0)

    slot1 = Slot(number="mkt l-2", destination="feu", level=1, status=0)

    slot2 = Slot(number="mkt l-3", destination="feu", level=1, status=0)

    slot3 = Slot(number="mkt l-4", destination="feu", level=1, status=0)

    slot4 = Slot(number="mkt l-5", destination="feu", level=1, status=0)

    slot5 = Slot(number="mkt l-6", destination="feu", level=1, status=0)

    slot6 = Slot(number="mkt l-7", destination="feu", level=1, status=0)

    slot7 = Slot(number="mkt l-8", destination="feu", level=1, status=0)

    slot8 = Slot(number="mkt m-1", destination="feu", level=1, status=0)

    slot9 = Slot(number="mkt m-2", destination="feu", level=1, status=0)

    slot10 = Slot(number="mkt m-3", destination="feu", level=1, status=0)

    slot11 = Slot(number="mkt m-4", destination="feu", level=1, status=0)

    slot12 = Slot(number="mkt m-5", destination="feu", level=1, status=0)

    slot13 = Slot(number="mkt m-6", destination="feu", level=1, status=0)

    slot14 = Slot(number="mkt m-7", destination="feu", level=1, status=0)

    slot15 = Slot(number="mkt m-8", destination="feu", level=1, status=0)

    slot16 = Slot(number="mkt m-9", destination="feu", level=1, status=0)

    slot17 = Slot(number="mkt m-10", destination="feu", level=1, status=0)

    slot18 = Slot(number="mkt m-11", destination="feu", level=1, status=0)

    slot19 = Slot(number="mkt m-12", destination="feu", level=1, status=0)

    slot20 = Slot(number="mkt m-13", destination="feu", level=1, status=0)

    slot21 = Slot(number="mkt r-1", destination="feu", level=1, status=0)

    slot22 = Slot(number="mkt r-2", destination="feu", level=1, status=0)

    slot23 = Slot(number="mkt r-3", destination="feu", level=1, status=0)

    slot24 = Slot(number="mkt r-4", destination="feu", level=1, status=0)

    slot25 = Slot(number="mkt r-5", destination="feu", level=1, status=0)

    slot26 = Slot(number="mkt r-6", destination="feu", level=1, status=0)

    slot27 = Slot(number="mkt r-7", destination="feu", level=1, status=0)


    db.session.add(register)
    db.session.add(dest)
    db.session.add(dest1)
    db.session.add(dest2)
    db.session.add(dest3)
    db.session.add(dest4)
    
    db.session.add(slot)
    db.session.add(slot1)
    db.session.add(slot2)
    db.session.add(slot3)
    db.session.add(slot4)
    db.session.add(slot5)
    db.session.add(slot6)
    db.session.add(slot7)
    db.session.add(slot8)

    db.session.add(slot9)
    db.session.add(slot10)
    db.session.add(slot11)
    db.session.add(slot12)
    db.session.add(slot13)
    db.session.add(slot14)
    db.session.add(slot15)
    db.session.add(slot16)
    db.session.add(slot17)
    db.session.add(slot18)
    db.session.add(slot19)
    db.session.add(slot20)

    db.session.add(slot21)
    db.session.add(slot22)
    db.session.add(slot23)
    db.session.add(slot24)
    db.session.add(slot25)
    db.session.add(slot26)
    db.session.add(slot27)

    db.session.commit()
    return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run(port=int(os.environ['PORT']), host='0.0.0.0')

    # port=int(os.environ['PORT']), host='0.0.0.0'