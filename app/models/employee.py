from app.extensions import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique = True)
    phone_number = db.Column(db.String(11), unique = True)
    position = db.Column(db.String(40))
    shift = db.Column(db.DateTime)
    birth_day = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f'<Employee {self.name}>'