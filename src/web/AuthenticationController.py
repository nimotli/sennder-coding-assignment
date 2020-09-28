import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
import src.service.AuthenticationService as authenticationService
import json
# from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods= ['POST'])
def register():
    return authenticationService.register(request.json)