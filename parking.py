import flask, flask.views
from flask import render_template
from flask import session, redirect
import os

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def facebook_login():
    return flask.render_template('index.html',scheme="dark")

if __name__ == '__main__':
    app.debug = True
    app.run(port=int(os.environ['PORT']), host='0.0.0.0')

    # port=int(os.environ['PORT']), host='0.0.0.0'