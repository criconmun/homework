from flask import Flask, redirect, render_template

from homework import visits

app = Flask(__name__)


@app.route("/")
def index():
    visits.increment()
    return render_template('index.html', number_of_visits = visits.count())

@app.route("/reset")
def reset():
    visits.reset()
    return redirect('/')

@app.route("/ping")
def ping():
    return 'pong'

if __name__ == "__main__":
    app.run()