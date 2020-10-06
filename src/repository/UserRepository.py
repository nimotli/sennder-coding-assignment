from src.domain.User import User
from src.repository.Repository import Repository

class UserRepository(Repository):

    def __init__(self):
        super().__init__(User)

    def findByUserName(self,username):
        user = User.query.filter_by(username=username).first()
        return user
