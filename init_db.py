from app import Submission, db

db.drop_all()
db.create_all()

submission1=Submission(group_id=1,group_hash='1234ef56',result=71.46252)
submission2=Submission(group_id=2,group_hash='4213gh65',result=87.46252)
submission3=Submission(group_id=3,group_hash='4333fa55',result=81.46252)
submission4=Submission(group_id=2,group_hash='4333fa55',result=83.46252)
submission5=Submission(group_id=2,group_hash='4333fa55',result=88.46252)
db.session.add_all([submission1,submission2,submission3, submission4, submission5])
db.session.commit()