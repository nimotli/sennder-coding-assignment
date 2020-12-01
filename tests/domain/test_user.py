import sys
print(sys.path)
from src.domain.User import User

def test_new_user():
    user = User('username','password')
    assert user.username == 'username'
    assert user.password == 'password'

def test_to_json():
    user = User('username','password')
    userJson = user.to_json()
    assert user.username == userJson.get('username')
    assert user.password == userJson.get('password')