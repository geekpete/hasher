import flask
from flask import render_template
import random,string,getpass,passlib,string
from passlib.hash import sha512_crypt

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/passwordhash')
@app.route('/passwordhash/<plaintextpassword>')
def passwordhash(plaintextpassword=None):
    if plaintextpassword:
        return sha512_crypt.encrypt("%s" % plaintextpassword)
    else:
        return "Usage: http://yourservername/passwordhash/yoursecretpassword"



if __name__ == '__main__':
    app.run(debug=True)
