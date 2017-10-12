from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'itsasecret'
mysql = MySQLConnector(app,'emails')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate/', methods=['POST'])
def validate():

    # If the email format is invalid
    if not email_regex.match(request.form['email']):
        flash(u'You entered an invalid email format! Please enter a proper email address and resubmit the form!', 'invalid')
        return redirect('/')
    
    # Check the database for the email record
    query = "SELECT email FROM emails WHERE email = :email"
    data = {'email': request.form['email']}
    result = mysql.query_db(query, data)
    print len(result)

    # If the query result length is greater than 0, confirm
    if len(result) != 0:
        flash(u'Congratulations! We found your email on the list.', 'yes')
        return redirect('/')
    
    # If the query result length is 0, inform and add
    else:
        flash(u'Your email is not listed! Adding now...','no')
        query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        return redirect('/')

# Email list
@app.route('/list/')
def list():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('list.html', emails=emails)


app.run(debug=True)