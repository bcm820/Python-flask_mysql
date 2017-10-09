
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'counter123456789'

@app.route('/')
def index():
    session['random'] = random.randrange(0, 101)
    return render_template("index.html")

@app.route('/guess/', methods=['post'])
def guess():
    session['ask'] = int(request.form['ask'])
    return redirect ('/result/')

@app.route('/result/')
def result():
    if session['ask'] < session['random']:
        return render_template("no.html", answer='Too Low!')
    if session['ask'] > session['random']:
        return render_template("no.html", answer='Too High!')
    else:
        answer = str(session['ask']) + " was the number!"
        return render_template("yes.html", answer=answer)

app.run(debug=True)