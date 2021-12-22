from flask import Flask, render_template
import flask
from flask import request;
from posts_data import books as data

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    #return render_template('home.html',books=data)
    return flask.jsonify(data)


# Create another route
@app.route("/about")
def about():
    return render_template('about.html',title="about")


@app.route("/login", methods=["POST"], strict_slashes=False)
def login():
    input_json = request.get_json(force=True) 
    print ('data from client:', input_json)
    dictToReturn = {'success':True}
    return flask.jsonify(dictToReturn)