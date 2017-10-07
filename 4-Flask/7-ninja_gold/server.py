
from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'counter123456789'

@app.route('/')
def index():
    try:
        session['gold'] += 0
    except:
        session['gold'] = 0
        session['activities'] = ""
    return render_template('index.html')

@app.route('/process/', methods=['post'])
def process():
    
    if request.form['building'] == 'farm':
        find = random.randrange(10, 21)
        session['gold'] += find
        session['activities'] += "Earned {} gold from the farm! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))

    if request.form['building'] == 'cave':
        find = random.randrange(5, 11)
        session['gold'] += find
        session['activities'] += "Earned {} gold from the cave! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))

    if request.form['building'] == 'house':
        find = random.randrange(2, 6)
        session['gold'] += find
        session['activities'] += "Earned {} gold from the house! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))

    if request.form['building'] == 'casino':
        find = random.randrange(0, 51)
        gamble = random.randrange(0,2)

        if gamble == 0:
            session['gold'] -= find
            session['activities'] += "Entered a casino and lost {} gold. Ouch! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))
        else:
            session['gold'] += find
            session['activities'] += "Entered a casino and won {} gold! Yesss! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))

    return redirect ('/')

app.run(debug=True)