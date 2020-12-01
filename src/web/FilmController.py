from flask import Blueprint
import src.service.FilmService as FilmService
from src.config.Environment import cache
from flask_jwt import jwt_required
from flask import jsonify,render_template

bp = Blueprint('film', __name__, url_prefix='/')

@bp.route('api/films', methods= ['GET'])
@cache.cached(timeout=60)
def get_all_films():
    return jsonify(FilmService.get_all_films())

@bp.route('/movies', methods= ['GET'])
def render_movies():
    return render_template('index.html')
