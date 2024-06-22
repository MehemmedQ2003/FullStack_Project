from flask import Blueprint

technologies_bp = Blueprint('technologies', __name__, url_prefix='/technologies', template_folder='templates', static_folder='static')

from . import routes