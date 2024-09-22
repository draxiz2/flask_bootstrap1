from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("html_flask.html")

@app.route('/contatos')
def contatos():
    return render_template("contatos_flask.html")

@app.route('/sobre')
def sobre():
    return render_template("html_sobre.html")

if __name__ == "__main__":
    app.run(debug=True)
