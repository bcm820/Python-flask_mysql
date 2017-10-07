
from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'itsasecret'

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/result/', methods=['POST'])
def form():

    # first
    # last
    # email
    # password
    # confirm

    # all fields required -- none blank (len)
    # first and last cannot contain numbers
    # password should be more than 8 chars (len)
    # password and password conf should match
    # email should be valid (regex)

    # IF improper submission, redirect to form and show the error above the form that asks the user to correct the info
    
    if len(request.form['name']) < 1:
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