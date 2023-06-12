from app.extensions import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    brand = db.Column(db.String(80))
    quantity = db.Column(db.Double)
    price = db.Column(db.Doule)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='items')
    
    def __repr__(self):
        return f'<Item {self.name}>'