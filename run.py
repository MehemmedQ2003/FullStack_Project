from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from admin import admin_bp
from app import app_bp
from models import db
from admin.routes import *
from app.routes import *
from flask_ckeditor import CKEditor

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tawheed.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']='mysecretkey'
    db.init_app(app)
    ckeditor = CKEditor(app)
    migrate = Migrate(app, db)
    app.register_blueprint(admin_bp)
    app.register_blueprint(app_bp)
    
    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)