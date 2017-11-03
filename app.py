from flask import Flask, render_template
from twitter.raw import *
from price.raw import *

app = Flask(__name__)

# basic test of react


@app.route("/")
def index():
    return render_template('index.html')

# basic test of filtering bootstrap 3 panels


@app.route("/grid")
def grid():
    return render_template('grid.html')


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    return render_template('dashboard.html', tweets = Tweets(['ethereum', 'bitcoin', 'litecoin']).get_tweets(),
                           btc_price="${0:,.2f}".format(Prices('BTC').last_price()),
                           btc_change="${0:,.2f}".format(Prices('BTC').last_price() - Prices('BTC').first_price()),
                           output=Prices('BTC').widget_graph())

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