from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://kaysiz:UwSJK1rAMao12tqE@matcha-6rlvv.mongodb.net/test?retryWrites=true&w" \
                          "=majority "
mongo = PyMongo(app)

from app.views import views, user_views

