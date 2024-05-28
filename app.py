import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


#### RELATIONSHIPS AND MODELS

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    group_id = db.Column(db.Integer)
    group_hash=db.Column(db.String(8))
    result = db.Column(db.Float)
    def __repr__(self):
        return f'<Submission: "{self.group_id}, {self.timestamp},{self.result} ">'
    


@app.route('/')
def index():
    submissions = list()
    results=list()
   
    for group_id in [1,2,3]:
        submissions.append(Submission.query.filter_by(group_id=group_id).order_by(Submission.result).first())
        
    return render_template('index.html', submissions = submissions, currdt=datetime.now())