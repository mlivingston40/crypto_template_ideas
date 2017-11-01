from flask import Flask, render_template
from twitter.raw import *

app = Flask(__name__)

# basic test of react


@app.route("/")
def index():
    return render_template('index.html')

# basic test of filtering bootstrap 3 panels


@app.route("/grid")
def grid():
    return render_template('grid.html')

# extension of grid


@app.route("/home", methods=['GET', 'POST'])
def home():

    test = Tweets(['ethereum', 'bitcoin'])

    tweets = test.get_tweets()

    return render_template('test.html',tweets = tweets)

@app.route("/bitcoin", methods=['GET', 'POST'])
def bitcoin():
    return render_template('bitcoin.html')

@app.route("/ethereum", methods=['GET', 'POST'])
def ethereum():
    return render_template('ethereum.html')

@app.route("/litecoin", methods=['GET', 'POST'])
def litecoin():
    return render_template('litecoin.html')

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(debug=True)