class FilmDTO:
    
    def __init__(self,id,title,description,director,producer,release_date,rt_score,people):
        self.id=id
        self.title=title
        self.description=description
        self.director=director
        self.producer=producer
        self.release_date=release_date
        self.rt_score=rt_score
        self.people=people

    def __repr__(self):
        return '<Film %r>' % self.title

    def to_json(self):
        json_user = {
            'id': self.id,
            'title': self.title ,
            'description': self.description ,
            'director': self.director ,
            'producer': self.producer ,
            'release_date':self.release_date ,
            'rt_score': self.rt_score ,
            'people': self.people 
        }
        return json_user