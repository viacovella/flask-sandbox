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



#### RELATIONSHIPS AND MODELS

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    group_id = db.Column(db.Integer)
    group_hash=db.Column(db.String(8))
    result = db.Column(db.Float)
    def __repr__(self):
        return f'<Submission: "{self.group_id}, {self.timestamp},{self.result} ">'
    
#### VIEWS

@app.route('/')
def index():

    submissions = list()
    for group_id in list(dict.fromkeys([submission.group_id for submission in Submission.query.order_by(Submission.group_id).all()])):
        curr_sub=Submission.query.filter_by(group_id=group_id).order_by(Submission.timestamp.desc()).first()
        submissions.append([curr_sub.result,curr_sub.group_id, curr_sub.timestamp.strftime('%Y-%m-%d %H:%M')])
    submissions.sort(reverse=True)
    print(submissions)
    return render_template('index.html', submissions = submissions)


@app.route('/group/<int:id>')
def RetrieveSingleGroup(id):
    sg_submissions = Submission.query.filter_by(group_id=id).all()
    if sg_submissions:
        return render_template('sgroupsubmissions.html', group_id=id, sg_submissions = sg_submissions, sg_submissions_len=len(sg_submissions))
    return f"Group {id} did not submit anything"


# CRUD operations
#### CREATE
@app.route('/group/create/', methods=['POST'])
def create():
    request_data = request.get_json()

    group_id = None
    group_hash = None
    result = None
    
    if request_data:
        if 'group_id' in request_data:
            group_id = request_data['group_id']

        if 'group_hash' in request_data:
            group_hash = request_data['group_hash']

        if 'result' in request_data:
            result = request_data['result']
    
    asubmission = Submission(group_id=int(group_id),group_hash=group_hash,result=float(result))
    db.session.add(asubmission)
    db.session.commit()
    
    return '''
           Group {} sent in a submission with a result of {}'''.format(group_id, result)