from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix='/home', template_folder='templates', static_folder='static')

from . import routes