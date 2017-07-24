from flask import Flask
from flask import request
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app .route('/user/<name>/<age>')
def user(name, age):
    print name
    print age
    rs = '<h1>Hello, %s%s!</h1>' % (name, age)
    print rs
    return rs


@app.route('/a')
def index1():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your brower is %s</p>' % user_agent


if __name__ == '__main__':
    manager.run()
