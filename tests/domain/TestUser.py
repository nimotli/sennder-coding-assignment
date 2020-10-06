import sys
print(sys.path)
from src.domain.User import User

def testNewUser():
    user = User('username','password')
    assert user.username == 'username'
    assert user.password == 'password'