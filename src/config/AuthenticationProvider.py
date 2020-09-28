from src.domain.User import User
from werkzeug.security import check_password_hash, generate_password_hash

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password,password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)