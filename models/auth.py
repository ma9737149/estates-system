from flask_login import UserMixin
from app.extensions import db
from datetime import datetime

class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80) , unique = True , nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow , nullable = False)  
    phone_number = db.Column(db.String(12) , unique=True , nullable = False)
    active = db.Column(db.Integer , unique=False , nullable = False , default = 0)
    role = db.Column(db.String(20), unique=False , nullable = False , default = 'user')
    profile_image = db.Column(db.String(30) , unique = False , nullable = True , default = 'users/imgs/default-img.png')

    def __repr__(self) -> str:
        return f'User(id={self.id} , username={self.username} , email = {self.email} , phone_number = {self.phone_number} )'

