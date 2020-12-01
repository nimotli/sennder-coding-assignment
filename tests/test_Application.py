import sys
from os.path import dirname, abspath
sys.path.insert(0,dirname(dirname(abspath(__file__))))
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
import tempfile
from src import create_app
import os

@pytest.fixture(scope='session')
def flask_app(request):
    app = create_app('test')

    with app.test_client() as client:
        yield client
