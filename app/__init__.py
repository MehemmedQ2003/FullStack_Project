from flask import Blueprint

app_bp = Blueprint('app', __name__, url_prefix='/', template_folder='templates', static_folder='static', static_url_path='app/static')


from . import routes