from flask import Blueprint

works_bp = Blueprint('works', __name__, url_prefix='/works', template_folder='templates', static_folder='static')

from . import routes