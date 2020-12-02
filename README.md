# CODING ASSIGNMENT

Allright, this is my solution for the coding assignment.

### Setup
- Clone the project
- Build the image
```
docker build -t senndercodingassignment:latest .
```
- run the image
```
docker run -it -p 8000:5000 senndercodingassignment
```
- the main page is on http://localhost:8000/movies
- or you can checkout the api response directly on http://localhost:8000/api/films


### Api
The main part of the app is the "/api/films" api
the returned data is formated as follow:
```json
[
    {
        "description": "filler description",
        "director": "director",
        "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
        "people": [
            {
                "age": "13",
                "eye_color": "Black",
                "gender": "Male",
                "hair_color": "Brown",
                "id": "fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
                "name": "Pazu"
            }
        ],
        "producer": "Isao Takahata",
        "release_date": "1986",
        "rt_score": "95",
        "title": "Castle in the Sky"
    }
]
```


### About

While the front end part is a complete eye sore i believe the back end is decently clean and structured. the architecture i went with is inspired from a java framework (JHIPSTER) with the code being split into 3 layers web,service and repository with a linear import path (web <= service <= repository), so this is a checkmark on one of the pricipals of a REST api.
Caching was hinted at, in the assignment's description so i just followed the instructions and added it to the main api.
I also added some basic unit tests and a JWT authentication that i ended up not implementing on the front end.


