from flask import Flask, render_template, flash

app = Flask(__name__)

app.secret_key = 'your_secret_key'

@app.route("/")
def hello_world():
    flash("Hello ji")
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)