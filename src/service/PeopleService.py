from urllib.request import urlopen
from src.service.dto.PeopleDTO import PeopleDTO
import json


def get_all_people_json():
    with urlopen('https://ghibliapi.herokuapp.com/people') as peopleRaw:
        data = json.loads(peopleRaw.read().decode())
    return data

def get_all_people(people_data = get_all_people_json):
    data = list(people_data())
    films = map(lambda d: PeopleDTO(d['id'], d['name'], d['gender'], d['age'], d['eye_color'], d['hair_color'], d['films']), data)
    return list(films)