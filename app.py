import os
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = "DE_Tickets_DB"
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tickets')
def get_tickets():
    return render_template("tickets.html", tickets=DE_Tickets_DB.Coll_Tickets.find())
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)