
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def form():
    return render_template('success.html',
        name = request.form['name'],
        language = request.form['language'],
        comment = request.form['comment']
        )

# @app.route('/success')
# def success():
#     return render_template("success.html")

app.run(debug=True)