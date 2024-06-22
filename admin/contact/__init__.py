from flask import Blueprint

contact_bp = Blueprint('contact', __name__, url_prefix='/contact', template_folder='templates', static_folder='static')

from . import routes