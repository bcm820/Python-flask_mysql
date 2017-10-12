from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector  # import the Connector function

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb') # connect mysql & pass DB name into function

# Friends list
@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)


# Friend profile
@app.route('/<friend_id>/')
def show(friend_id):
    
    # Write query to select specific user by id.
    # Wherever we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}

    # Run query with inserted data.
    friends = mysql.query_db(query, data)

    # Friends should be a list with a single object, so we pass the value at [0] to our template under alias one_friend.
    return render_template('friend.html', one_friend=friends[0])


# Add friend to list
@app.route('/add/', methods=['POST'])
def add():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (name, age, friend_since, created_at, updated_at) VALUES (:name, :age, :friend_since, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
             'friend_since': request.form['friend_since']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')


# Update friend profile
@app.route('/update/<friend_id>/', methods=['POST'])
def update(friend_id):
    # Say we wanted to update a specific record, we could create another page and add a form that would submit to the following route
    query = "UPDATE friends SET name = :name, age = :age, friend_since = :friend_since WHERE id = :id"
    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
             'friend_since': request.form['friend_since'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')


# Delete friend
@app.route('/delete/<friend_id>/', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')





app.run(debug=True)