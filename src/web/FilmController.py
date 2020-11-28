import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
import src.service.FilmService as FilmService
from flask import jsonify

bp = Blueprint('film', __name__, url_prefix='/api')

@bp.route('/films', methods= ['GET'])
def get_all_films():
    return jsonify(FilmService.get_all_films())


@bp.route('/people-by-films', methods= ['GET'])
def get_people_by_film():
    return FilmService.get_people_by_movie()

