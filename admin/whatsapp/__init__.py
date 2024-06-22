from flask import Blueprint

whatsapp_bp = Blueprint('whatsapp', __name__, url_prefix='/whatsapp', template_folder='templates', static_folder='static')

from . import routes