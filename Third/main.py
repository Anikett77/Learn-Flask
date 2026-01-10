from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Aniket"
    language = "Python"
    luckynos = [1,5,76,86,99,100]
    footer = "<p> Cpoyright 2025 </p> | All rights reserved"
    return render_template("index.html", name=name, lang=language, lucky=luckynos , footer=footer)

app.run(debug=True)