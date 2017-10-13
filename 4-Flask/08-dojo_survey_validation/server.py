
from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'itsasecret'

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/result/', methods=['POST'])
def form():

    if len(r..equest.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')

    if len(request.form['comment']) < 1:
        flash("Comment field cannot be empty!")
        return redirect('/')

    if len(request.form['comment']) > 120:
        flash("Comment field cannot be longer than 120 characters!")
        return redirect('/')
        
    else:
        session['name'] = request.form['name']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/success/')

@app.route('/success/')
def result():
    return render_template("success.html")

app.run(debug=True)