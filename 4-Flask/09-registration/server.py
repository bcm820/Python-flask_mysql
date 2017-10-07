
from flask import Flask, render_template, request, redirect, flash, session
import re

app = Flask(__name__)
app.secret_key = 'itsasecret'

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def root():
    session['flash_count'] = 0  # Set flash counter to determine # of errors
    return render_template("index.html")

@app.route('/process/', methods=['post'])
def form():

    # first - no numbers, not blank
    if len(request.form['first']) < 1:
        flash(u'You must fill out this field.', 'first')
        session['flash_count'] += 1 # Log error in counter
        session['first'] = ""   # Clear invalid entry
    elif not request.form['first'].isalpha():
        flash(u"Your first name should only include letters.", 'first')
        session['flash_count'] += 1
        session['first'] = ""
    else:
        session['first'] = request.form['first']    # Store valid entry

    # last - no numbers, not blank
    if len(request.form['last']) < 1:
        flash(u'You must fill out this field.', 'last')
        session['flash_count'] += 1
        session['last'] = ""
    elif not request.form['last'].isalpha():
        flash(u"Your first name should only include letters.", 'last')
        session['flash_count'] += 1
        session['last'] = ""
    else:
        session['last'] = request.form['last']

    # email - format (regex), not blank
    if len(request.form['email']) < 1:
        flash(u'You must fill out this field.', 'email')
        session['flash_count'] += 1
        session['email'] = ""
    elif not email_regex.match(request.form['email']):
        flash(u'You entered an invalid email format.', 'email')
        session['flash_count'] += 1
        session['email'] = ""
    else:
        session['email'] = request.form['email']

    # password - not blank, more than 8 chars, at least 1 upper and 1 num
    if len(request.form['password']) < 8 or not request.form['password'].istitle() or request.form['password'].isalpha():
        flash(u'For security purposes, your password must be at least 9 characters with at least one uppercase letter and one number.', 'password')
        session['flash_count'] += 1
        session['password'] = ""
    else:
        session['password'] = request.form['password']

    # confirm - match password
    if not request.form['confirm'] == request.form['password']:
        flash(u'Your password confirmation does not match your initial password. Please re-enter both your password and confirmation.', 'confirm')
        session['flash_count'] += 1
        session['password'] = ""
        session['confirm'] = ""
    else:
        session['confirm'] = request.form['confirm']
    
    # confirm errors or confirm submission
    if session['flash_count'] > 0:
        flash('Registration incomplete. Check the form for errors and try again.', 'submit')
        return redirect('/')
    else:
        flash('Your registration is complete! Thanks for signing up!', 'submit')
        session['flash_count'] = 0
        return redirect('/')

app.run(debug=True)