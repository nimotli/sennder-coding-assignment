
from flask import Flask
from src.config.Blueprint import registerBluePrints
from flask_jwt import JWT, jwt_required, current_identity
from src.config.ApplicationProperties import getEnv
from src.config.DatabaseConfiguration import init_db
from src.config.Envirement import db,migrate
from src.config.AuthenticationProvider import authenticate,identity
import os
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    env = getEnv("dev")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = env['jwt_secret']
    app.config['JWT_AUTH_URL_RULE'] = env['auth_url']
    jwt = JWT(app, authenticate, identity)
    app = init_db(app,env)
    db.init_app(app)
    '''
    Add any created model that you want to be added to the migration-able models list
    '''
    from  src.domain import User
    migrate.init_app(app, db)
    app = registerBluePrints(app)
    return app