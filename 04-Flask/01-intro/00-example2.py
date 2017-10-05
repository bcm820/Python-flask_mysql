
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# our index route will handle rendering our form as HTML
@app.route('/')
def index():
    return render_template("index.html")

# our success route is the redirect after form submission
@app.route('/success')
def success():
    return render_template("success.html")

# our next route will handle our form submission
@app.route('/users', methods=['POST']) # unless GET, we must define HTTP method
def create_user():

    # confirm form input has been received
    print "Got Post Info"

    # set vars to form input
    name = request.form['name']
    email = request.form['email']
    print name
    print email

    # redirect user back to '/' route
    # MUST use redirect, or otherwise user can resubmit form data via refresh
    return redirect('/success')

# run our server
app.run(debug=True)