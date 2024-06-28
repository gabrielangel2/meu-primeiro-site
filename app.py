from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/amostras")
def amostras():
    return "<h1>site teste</h1>"


@app.route("/planos")
def planos():
    return "<h1>site teste</h1>"


@app.route("/agendamento")
def agendamento():
    return "<h1>site teste</h1>"


@app.route("/evento")
def evento():
    return "<h1>site teste</h1>"


@app.route("/instagram")
def instagram():
    return "<h1>site teste</h1>"


@app.route("/whatsapp")
def whatsapp():
    return "<h1>site teste</h1>"


if __name__ == "__main__":
    app.run(debug=True)
