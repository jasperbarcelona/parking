import flask, flask.views
from flask import render_template
from flask import session, redirect

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def facebook_login():
    return flask.render_template('index.html',data="hello")

if __name__ == '__main__':
    app.debug = True
    app.run()