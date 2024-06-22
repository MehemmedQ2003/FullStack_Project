from .home import home_bp
from .info import info_bp
from .technologies import technologies_bp
from .works import works_bp
from .contact import contact_bp
from .whatsapp import whatsapp_bp
from flask import Blueprint

admin_bp = Blueprint('admin', __name__,url_prefix='/admin', template_folder='templates', static_folder='static')

from . import routes

admin_bp.register_blueprint(home_bp)
admin_bp.register_blueprint(info_bp)
admin_bp.register_blueprint(technologies_bp)
admin_bp.register_blueprint(works_bp)
admin_bp.register_blueprint(contact_bp)
admin_bp.register_blueprint(whatsapp_bp)