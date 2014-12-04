import flask, flask.views
from flask import render_template, request
from flask import session, redirect
import os

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def facebook_login():
    return flask.render_template('index.html',scheme="dark")


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