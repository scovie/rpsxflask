# RPS x Flask
'''
Simple Flask based application that can be used as a next step up
from the basic "Hello, World!" app.

@scovie 7-Feb-2019
To learn more about Flask visit http://flask.pocoo.org/docs/1.0/quickstart/
'''
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method=='POST':
        return render_template('play.html', choice=rps())
    else:
        return render_template('play.html')

def rps():
    return random.randint(1, 3)

if __name__ == '__main__':
    app.run()