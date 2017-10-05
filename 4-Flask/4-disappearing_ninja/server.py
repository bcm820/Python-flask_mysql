
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/ninja')
def all():
    return render_template("all.html")

@app.route('/ninja/<color>')
def turtle(color):
    if color == "blue":
        return render_template("leonardo.html")
    if color == "orange":
        return render_template("michaelangelo.html")
    if color == "purple":
        return render_template("donatello.html")
    if color == "red":
        return render_template("raphael.html")
    else:
        return render_template("april.html")

app.run(debug=True)