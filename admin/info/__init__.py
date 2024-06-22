from flask import Blueprint

info_bp = Blueprint('info', __name__, url_prefix='/info', template_folder='templates', static_folder='static')

from . import routes