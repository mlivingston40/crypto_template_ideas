from flask import Flask, render_template

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


@app.route("/grid2")
def grid():
    return render_template('grid2.html')


if __name__ == "__main__":
    app.run()