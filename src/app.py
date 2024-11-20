
from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

@app.route("/index")
def index():
    return render_template('index.html')

