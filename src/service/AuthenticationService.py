from src.repository.UserRepository import UserRepository
from werkzeug.security import check_password_hash, generate_password_hash
from src.domain.User import User
from flask import jsonify,url_for

userRepository = UserRepository()

def register(dto):
    print(dto)
    user = User(dto["username"],generate_password_hash(dto["password"]))
    user.email = dto["email"]
    userRepository.save(user)
    return jsonify(user.to_json())