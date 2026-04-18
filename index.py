from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def About():
    return render_template("about.html")

@app.route('/contact')
def Contact():
    return render_template("contact.html")

app.run(debug=True)
