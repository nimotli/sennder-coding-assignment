from flask import Blueprint
import src.service.FilmService as FilmService
from src.config.Environment import cache
from flask_jwt import jwt_required
from flask import jsonify

bp = Blueprint('film', __name__, url_prefix='/api')

@bp.route('/films', methods= ['GET'])
@cache.cached(timeout=60)
def get_all_films():
    return jsonify(FilmService.get_all_films())


@bp.route('/people-by-films', methods= ['GET'])
def get_people_by_film():
    return FilmService.get_people_by_movie()

