from src.service.dto.PeopleDTO import PeopleDTO
import src.service.FilmService  as filmService


def test_get_all_films():
    def film_data():
        return [{
            'id':'film',
            'title':'title',
            'description':'description',
            'director':'director',
            'producer':'producer',
            'release_date':'release_date',
            'rt_score':'rt_score'
        }]
    def people_data():
        return [PeopleDTO('id', 'name', 'gender', 'age', 'eye_color', 'hair_color', ['films/film'])]
    all_films = filmService.get_all_films(film_data,people_data)
    assert all_films is not None
    assert len(all_films) == 1
    assert all_films[0]['id'] == 'film'
    assert all_films[0]['title'] == 'title'
    assert all_films[0]['description'] == 'description'
    assert all_films[0]['director'] == 'director'
    assert all_films[0]['producer'] == 'producer'
    assert all_films[0]['release_date'] == 'release_date'
    assert all_films[0]['rt_score'] == 'rt_score'
    assert all_films[0]['people'] is not None
    people = all_films[0]['people']
    assert len(people) == 1
    assert people[0]['id'] == 'id'
    assert people[0]['name'] == 'name'
    assert people[0]['gender'] == 'gender'
    assert people[0]['age'] == 'age'
    assert people[0]['eye_color'] == 'eye_color'
    assert people[0]['hair_color'] == 'hair_color'


def test_get_people_by_movie():
    people = [PeopleDTO('id', 'name', 'gender', 'age', 'eye_color', 'hair_color', ['films/film'])]
    people_by_film = filmService.get_people_by_movie(people)
    assert 'film' in people_by_film.keys()
    assert people_by_film['film'] is not None
    people = people_by_film['film'][0]
    assert people['id'] == 'id'
    assert people['name'] == 'name'
    assert people['gender'] == 'gender'
    assert people['age'] == 'age'
    assert people['eye_color'] == 'eye_color'
    assert people['hair_color'] == 'hair_color'

def test_get_people_by_film_dict():
    people = [PeopleDTO('id', 'name', 'gender', 'age', 'eye_color', 'hair_color', ['films/film'])]
    people_by_film_list = filmService.get_people_by_film_list(people)
    people_by_film = filmService.get_people_by_film_dict(people_by_film_list)
    assert people_by_film is not None

def test_get_people_by_film_list():
    people = [PeopleDTO('id', 'name', 'gender', 'age', 'eye_color', 'hair_color', ['films/film'])]
    people_by_film_list = filmService.get_people_by_film_list(people)
    assert people_by_film_list is not None
    assert len(people_by_film_list) == 1
    people = people_by_film_list[0]
    assert people[0] == 'films/film'
    assert people[1].id == 'id'
    assert people[1].name == 'name'
    assert people[1].gender == 'gender'
    assert people[1].age == 'age'
    assert people[1].eye_color == 'eye_color'
    assert people[1].hair_color == 'hair_color'