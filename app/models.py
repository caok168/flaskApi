from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    phone = db.Column(db.String(100),unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)
    uuid = db.Column(db.String(255),unique=True)
    # userlogs = db.relationship('Userlog',backref= 'user')
    # comments = db.relationship('Comment',backref= 'user')
    # moviecols = db.relationship('Moviecol', backref='user')

    def __repr__(self):
        return "<User %r>" % self.name


class Label(db.Model):
    __tablename__ = 'label'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    type = db.Column(db.String(64))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Label %r>" % self.name
