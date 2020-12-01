class PeopleDTO:
    
    def __init__(self,id,name,gender,age,eye_color,hair_color,films):
        self.id=id
        self.name=name
        self.gender=gender
        self.age=age
        self.eye_color=eye_color
        self.hair_color=hair_color
        self.films=films

    def __repr__(self):
        return '<People %r>' % self.name

    def to_json(self):
        json_user = {
            'id': self.id,
            'name': self.name ,
            'gender': self.gender ,
            'age': self.age ,
            'eye_color': self.eye_color ,
            'hair_color':self.hair_color ,
        }
        return json_user