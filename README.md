# CODING ASSIGNMENT

Allright, this is my solution for the coding assignment.

### Setup
- Clone the project
- Create a virtual env 
```
python -m venv venv
```
- Activate the virtual envirement
- Install the requirements
```
pip install -r requirements.txt
```
- Set the flask app path
```
set FLASK_APP=src
```
- start the app
```
flask run -p 8000
```
- To run the tests
```
pytest
```

### Api
The main part of the app is the "/api/films" api
the returned data is formated as follow:
```
json
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
Going to the next poing which is statelessness, which is achieved by not using any session based auth, and i went with a simple JWT based auth (not implement on the front-end yet).
Caching was hinted at, in the assignment's description so i just followed the instructions and added it to the main api.


