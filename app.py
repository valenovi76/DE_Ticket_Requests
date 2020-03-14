import os
from os import path
if path.exists("env.py"):
    import env
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME") 

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tickets')
def get_tickets():
    return render_template("tickets.html", tickets=mongo.db.Coll_Tickets.find())
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)