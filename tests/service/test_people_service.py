from src.service.dto.PeopleDTO import PeopleDTO
import src.service.PeopleService  as peopleService


def test_get_all_people():
    def people_data():
        return [{
            'id':'id',
            'name':'name',
            'gender':'gender',
            'age':'age',
            'eye_color':'eye_color',
            'hair_color':'hair_color',
            'films':'films/film'
        }]
    all_people = peopleService.get_all_people(people_data)
    assert all_people is not None
    assert len(all_people) == 1
    assert all_people[0].id == 'id'
    assert all_people[0].name == 'name'
    assert all_people[0].gender == 'gender'
    assert all_people[0].age == 'age'
    assert all_people[0].eye_color == 'eye_color'
    assert all_people[0].hair_color == 'hair_color'
    assert all_people[0].films == 'films/film'

