from src.config.Envirement import db
from flask import url_for
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        json_user = {
            # 'url': url_for('api.get_user', id=self.id),
            'username': self.username,
            'email': self.email,
            'password': self.password
        }
        return json_user