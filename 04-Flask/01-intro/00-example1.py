
### INTRODUCTION TO FLASK

#See accompanying '0-Notes.py'

# Import Flask to allow us to create our app.
# Also import render_template to allow us to render our HTML.
from flask import Flask, render_template

# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module. 'app' represents our web app. We use this variable to attach routing rules for our app.
app = Flask(__name__)

# The "@" symbol designates a "decorator" which attaches the function immediately following it to the '/' route.
@app.route('/')
# Whenever we send a request to localhost:5000/ it will run the function.

def hello_world():  # function attached to @app.route('/')
  
  # Renders HTML in 'templates' dir and returns it
  return render_template('index.html')

app.run(debug=True) # Run the app in debug mode.