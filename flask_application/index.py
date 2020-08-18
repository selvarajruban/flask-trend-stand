# To run the flask application
# set FLASK_APP=index.py
# python -m flask run

# http://127.0.0.1:5000/

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html')