from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'itsasecret'
mysql = MySQLConnector(app,'users')


# DOMAIN: Redirect to Index
@app.route('/')
def domain():
    return redirect('/users/')


### DISPLAY TEMPLATES ###

# INDEX: Display all records
@app.route('/users/')
def index():
    query = "SELECT * FROM users"
    all_users = mysql.query_db(query)
    return render_template('index.html', users=all_users)


# SHOW: Display one record
@app.route('/users/<user_id>/')
def show(user_id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {'id': user_id}
    user = mysql.query_db(query, data)
    return render_template('show.html', user=user[0])


### FORM TEMPLATES ###

# NEW (Registration Form)
# Fields: Name (full), Email
@app.route('/users/new/')
def new():
    query = "SELECT * FROM users"
    all_users = mysql.query_db(query)
    return render_template('new.html', users=all_users)


# EDIT (Update User Form) -- Duplicate from Reg. Form!!!
# Fields: Name (full), Email
@app.route('/users/<user_id>/edit/')
def edit(user_id):
    query = "SELECT * FROM users WHERE id = :id"
    data = {'id': user_id}
    user = mysql.query_db(query, data)
    return render_template('edit.html', user=user[0])


### POST QUERIES ###

# CREATE: Insert new record (& redirect to SHOW)
@app.route('/users/create/', methods=['POST'])
def create():
    
    # Query 1: Insert new record
    query = "INSERT INTO users (name, email, created_at, updated_at) VALUES (:name, :email, NOW(), NOW())"
    data = {
        'name': request.form['name'],
        'email': request.form['email']
        }
    mysql.query_db(query, data)

    # Query 2: Select for redirect to SHOW record
    query = "SELECT id FROM users WHERE email = :email"
    data = {'email': request.form['email']}
    user_id = mysql.query_db(query, data)

    # Note- When redirecting from var query data, call value via key!
    return redirect('/users/{}/'.format(user_id[0]['id']))
    
# UPDATE: Update record by ID
@app.route('/users/<user_id>/update/', methods=['POST'])
def update(user_id):
    
    query = "UPDATE users SET name = :name, email = :email WHERE id = :id"
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'id': user_id
        }
    mysql.query_db(query, data)
    return redirect('/users/{}/'.format(user_id))


# DESTROY: Delete record by ID
@app.route('/users/<user_id>/destroy/', methods=['POST'])
def destroy(user_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': user_id}
    mysql.query_db(query, data)
    return redirect('/users/')


app.run(debug=True)