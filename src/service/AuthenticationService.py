from src.config.Envirement import db
from werkzeug.security import check_password_hash, generate_password_hash
from src.domain.User import User
from flask import jsonify,url_for

def register(dto):
    print(dto)
    user = User()
    user.email = dto["email"]
    user.username = dto["username"]
    user.password = generate_password_hash(dto["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json())