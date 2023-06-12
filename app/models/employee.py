from app.extensions import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name
    # email
    # phone_number
    # position
    # shift
    # birth_day
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='items')