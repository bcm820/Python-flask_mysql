
from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re, md5, os, binascii

app = Flask(__name__)
app.secret_key = 'itsasecret'
mysql = MySQLConnector(app,'wall')
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



### Join GET & POST
@app.route('/join/')
def join():
    session['flash_count'] = 0  # Set counter for errors
    return render_template("join.html")

@app.route('/join/new/', methods=['POST'])
def new():

    # first - no numbers, not blank
    if len(request.form['first_name']) < 2:
        flash(u'Must be at least 2 characters.', 'first')
        session['flash_count'] += 1 # Log error in counter
        session['first_name'] = ""   # Clear invalid entry
    elif not request.form['first_name'].isalpha():
        flash(u"Only letters are allowed.", 'first')
        session['flash_count'] += 1
        session['first_name'] = ""
    else:
        session['first_name'] = request.form['first_name']    # Store entry

    # last - no numbers, not blank
    if len(request.form['last_name']) < 2:
        flash(u'Must be at least 2 characters.', 'last')
        session['flash_count'] += 1
        session['last_name'] = ""
    elif not request.form['last_name'].isalpha():
        flash(u"Only letters are allowed.", 'last')
        session['flash_count'] += 1
        session['last_name'] = ""
    else:
        session['last_name'] = request.form['last_name']

    # email - format (regex), not blank
    if len(request.form['email']) < 1:
        flash(u'No email address provided.', 'email')
        session['flash_count'] += 1
        session['email'] = ""
    elif not email_regex.match(request.form['email']):
        flash(u'Invalid address format.', 'email')
        session['flash_count'] += 1
        session['email'] = ""
    else:
        session['email'] = request.form['email']

    # password - not blank, more than 8 chars
    if len(request.form['password']) < 8:
        flash(u'Must be 8 or more characters.', 'password')
        session['flash_count'] += 1
        session['password'] = ""
    else:
        session['password'] = request.form['password']

    # confirm - match password
    if not request.form['confirm'] == request.form['password']:
        flash(u'Passwords do not match.', 'confirm')
        session['flash_count'] += 1
        session['password'] = ""
        session['confirm'] = ""
    else:
        session['confirm'] = request.form['confirm']
    
    # If errors, show errors
    if session['flash_count'] > 0:
        return redirect('/join/')

    # If no errors, add new user to DB
    else:
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

        return redirect('/wall/')

###



### Login GET & POST
@app.route('/')
def root():
    return render_template("index.html")

@app.route('/login/', methods=['POST'])
def login():

    # Error if the email format is invalid
    if not email_regex.match(request.form['email']):
        flash(u'Invalid address format.', 'email')
        return redirect('/')
    else:
        session['temp'] = request.form['email'] # temp email store

    # Query DB for the login info
    query = "SELECT id, email, password, salt FROM users WHERE email = :email LIMIT 1"
    data = {'email': request.form['email']}
    result = mysql.query_db(query, data)

    # If record found, verify password
    if len(result) != 0:
        if result[0]['password'] == md5.new(request.form['password'] + result[0]['salt']).hexdigest():
            session['user'] = result[0]['id']   # create session with ID
            session['temp'] = "" #empty temp email store
            return redirect('/wall/')
        else:
            flash(u'Password incorrect.', 'password')
            return redirect('/')
    else:
        flash(u'Account not found.', 'email')
        return redirect('/')

###



### Wall GET
@app.route('/wall/')
def wall():
    
    # Query for logged in user's information to display their data
    query_user = "SELECT * FROM users WHERE id = :id LIMIT 1"
    user_id = {'id': session['user']}
    user = mysql.query_db(query_user, user_id)

    # Query for messages
    query_messages = "SELECT users.id, messages.user_id, users.first_name, users.last_name, messages.id, messages.message, messages.created_at FROM users JOIN messages ON messages.user_id = users.id GROUP BY messages.id ORDER BY messages.id DESC"
    messages = mysql.query_db(query_messages)

    # Convert message time format
    for i in range (0,len(messages)):
        m_time = messages[i]["created_at"]
        messages[i]["created_at"] = m_time.strftime('%A %B %d, %Y at %-I:%M %p')

    # Query for comments
    query_comments = "SELECT users.first_name, users.last_name, comments.comment, comments.created_at, comments.message_id FROM users JOIN messages ON messages.user_id = users.id JOIN comments ON comments.message_id = messages.id GROUP BY comments.id ORDER BY comments.id ASC"
    comments = mysql.query_db(query_comments)

    # Convert comments time format
    for i in range (0,len(comments)):
        c_time = comments[i]["created_at"]
        comments[i]["created_at"] = c_time.strftime('%c')
        
    return render_template("wall.html", user=user[0], messages=messages, comments=comments)

###



### Wall POST
@app.route('/wall/logout/', methods=['POST'])
def logout():
    session['user'] = ""
    return redirect('/')

@app.route('/wall/message/', methods=['POST'])
def message():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
        'user_id': session['user'],
        'message': request.form['message'],
    }
    mysql.query_db(query, data)
    return redirect('/wall/')

@app.route('/wall/comment/', methods=['POST'])
def comment():
    query = "INSERT INTO comments (user_id, comment, message_id, created_at, updated_at) VALUES (:user_id, :comment, :message_id, NOW(), NOW())"
    data = {
        'user_id': session['user'],
        'comment': request.form['comment'],
        'message_id': request.form['message_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall/')
###




app.run(debug=True)