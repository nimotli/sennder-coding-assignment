from urllib.request import urlopen
from src.service.dto.FilmDTO import FilmDTO
import src.service.PeopleService as PeopleService
import json


def get_all_films_json():
    with urlopen('https://ghibliapi.herokuapp.com/films') as filmRaw:
        data = json.loads(filmRaw.read().decode())
    return data

def get_all_films(film_data = get_all_films_json,people_data = PeopleService.get_all_people):
    data = film_data()
    allPeople = people_data()
    
    people_by_film = get_people_by_movie(allPeople)
    films = list(map(lambda d: 
        FilmDTO(d['id'], d['title'], d['description'], d['director'], d['producer'], d['release_date'], d['rt_score'],
        people_by_film[d['id']] if d['id'] in people_by_film.keys() is not None else []
        ).to_json()
    , data))
    return films

def get_people_by_movie(allPeople):
    peopleByFilmList = get_people_by_film_list(allPeople)
    peopleByFilm = get_people_by_film_dict(peopleByFilmList)
    return peopleByFilm

def get_people_by_film_dict(peopleByFilmList):
    peopleByFilm = dict()
    for p_by_f in peopleByFilmList:
        key = p_by_f[0].split('films/')[1]
        if key in peopleByFilm.keys():
            peopleByFilm[key].append(p_by_f[1].to_json())
        else:
            peopleByFilm[key]=[p_by_f[1].to_json()]
    return peopleByFilm

def get_people_by_film_list(allPeople):
    peopleByFilmList = []
    for p in allPeople:
        for filmId in p.films:
            peopleByFilmList.append([filmId,p])
    return peopleByFilmList
