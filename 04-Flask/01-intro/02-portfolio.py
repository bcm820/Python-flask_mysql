
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return 'I am a Python web developer and love going to hackathons in my spare time. I love making things and meeting new people! People might be surprised to learn that I own a horse and used to be a horse trainer!'

app.run(debug=True)