
from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re, md5, os, binascii

app = Flask(__name__)
app.secret_key = 'itsasecret'
mysql = MySQLConnector(app,'mydb')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login/', methods=['POST'])
def login():
    
    # If the email format is invalid
    if not email_regex.match(request.form['email']):
        flash(u'You entered an invalid email format.', 'email')
        return redirect('/')

    # Query DB for the login info
    query = "SELECT email, password, salt, id FROM users WHERE email = :email LIMIT 1"
    data = {'email': request.form['email']}
    result = mysql.query_db(query, data)

    # If record found, check password
    if len(result) != 0:
        if result[0]['password'] == md5.new(request.form['password'] + result[0]['salt']).hexdigest():

            # If verified, create single session variable with user ID
            session['user'] = result[0]['id']
            return redirect('/confidential/')

        else:
            flash(u'The password you entered cannot be verified.', 'password')
            return redirect('/')

    else:
        flash(u'Your account was not found in our database.', 'email')
        return redirect('/')

#

@app.route('/confidential/')
def confidential():
    # Query for logged in user's information to display their data
    query = "SELECT * FROM users WHERE id = :id LIMIT 1"
    data = {'id': session['user']}
    user = mysql.query_db(query, data)
    return render_template("confidential.html", user=user[0])

@app.route('/logout/', methods=['POST'])
def logout():
    session['user'] = ""
    return redirect('/')

@app.route('/registration/')
def registration():
    session['flash_count'] = 0  # Set flash counter to determine # of errors
    return render_template("registration.html")
#

@app.route('/registration/add/', methods=['POST'])
def add():

    # first - no numbers, not blank
    if len(request.form['first_name']) < 2:
        flash(u'Your first name must be at least 2 characters.', 'first')
        session['flash_count'] += 1 # Log error in counter
        session['first_name'] = ""   # Clear invalid entry
    elif not request.form['first_name'].isalpha():
        flash(u"Your first name should only include letters.", 'first')
        session['flash_count'] += 1
        session['first_name'] = ""
    else:
        session['first_name'] = request.form['first_name']    # Store valid entry

    # last - no numbers, not blank
    if len(request.form['last_name']) < 2:
        flash(u'Your last name must be at least 2 characters.', 'last')
        session['flash_count'] += 1
        session['last_name'] = ""
    elif not request.form['last_name'].isalpha():
        flash(u"Your first name should only include letters.", 'last')
        session['flash_count'] += 1
        session['last_name'] = ""
    else:
        session['last_name'] = request.form['last_name']

    # email - format (regex), not blank
    if len(request.form['email']) < 1:
        flash(u'You must provide your email address.', 'email')
        session['flash_count'] += 1
        session['email'] = ""
    elif not email_regex.match(request.form['email']):
        flash(u'You entered an invalid email format.', 'email')
        session['flash_count'] += 1
        session['email'] = ""
    else:
        session['email'] = request.form['email']

    # password - not blank, more than 8 chars, at least 1 upper and 1 num
    if len(request.form['password']) < 8:
        flash(u'Your password must be at least 8 letters.', 'password')
        session['flash_count'] += 1
        session['password'] = ""
    else:
        session['password'] = request.form['password']

    # confirm - match password
    if not request.form['confirm'] == request.form['password']:
        flash(u'Your passwords do not match.', 'confirm')
        session['flash_count'] += 1
        session['password'] = ""
        session['confirm'] = ""
    else:
        session['confirm'] = request.form['confirm']
    
    # Show errors or submit and go to login page
    if session['flash_count'] > 0:
        return redirect('/registration/')

    else:
        
        # Add info to DB
        query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
        salt =  binascii.b2a_hex(os.urandom(15))
        data = {
             'first_name': session['first_name'],
             'last_name': session['last_name'],
             'email': session['email'],
             'password': md5.new(session['password'] + salt).hexdigest(),
             'salt': salt
           }
        mysql.query_db(query, data)

        # Clear flash_count and form inputs
        session['flash_count'] = 0
        session['first_name'] = ""
        session['last_name'] = ""
        session['email'] = ""
        session['password'] = ""
        session['confirm'] = ""

        return redirect('/')

#

app.run(debug=True)