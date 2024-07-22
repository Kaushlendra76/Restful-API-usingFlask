from app import db

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    parent_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255)) 
    interest = db.Column(db.String(255))  

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
    parent = db.relationship('Parent', backref=db.backref('children', lazy=True))


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    age_group = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    vlog_url = db.Column(db.String(200), nullable=True)
