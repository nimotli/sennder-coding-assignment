from src.config.Environment import db

class Repository:

    def __init__(self, EntityType):
        self.EntityType = EntityType

    def save(self,entity):
        db.session.add(entity)
        db.session.commit()

    def findById(self,id):
        user = self.EntityType.query.get(id)
        
    def findAll(self):
        user = self.EntityType.query.all()

    def delete(self,id):
        user = self.EntityType.query.get(id)
        db.session.delete(user)
        db.session.commit()