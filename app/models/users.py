from app.extensions import db

class Users(db.Model):
    
    __tablename__ = 'users'
    
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))
    userIcon = db.Column(db.String(50))
    
    def __repr__(self):
        return f'<Users {self.name}>'