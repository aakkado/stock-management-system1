from app.extensions import db

class User(db.Model):
    id=db.Column(db.Interger, primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))