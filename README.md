# Flask Application Structure (DONT USE YET ONGOING WORK)

It's an easy to understand layered Flask architecture for application backends, inspired by Jhipster

### Features
  - Layered Web->Service->Repository Architecture
  - Multiple database sources and types
  - Migration
  - ORM
  - JWT authentication
  - Testing
  - Multiple Profiles for multiple environment

### Installation

- Clone this repo
- Create a python virtual environment (Optional)
- Activate the virtual environment (Optional)
- Run : pip install -r requirements.tx

(write the installation steps for all OS)
### Setup
(write the setup steps for all OS)

### Migration : 
- Create the entity in ./src/domain/
- Add it to the import list in the create-app function in src/__init__.py
- Run : flask db init -d resources/migration/main
- Run : flask db migrate -d resources\migration\main -m "migration name"
- Run : flask db upgrade

### ORM

### Authentication
#### JWT
- Requires a valid database connection and to already launch a migration
- /register to create a new user
- /api/authenticate [POST] to get jwt token
- Send username and password
- Pass the recieved token as a header "Authorization":"JWT your_generated_token"

### Database Configuration


### Models


### Profiles


### Routing

