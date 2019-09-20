from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template('./user/index.html')


@app.route("/about")
def about():
    return "Hello world!!"
