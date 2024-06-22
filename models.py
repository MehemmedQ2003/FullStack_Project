from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    
class Works(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.Text, nullable=False)
    
class Technologies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    address_link = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    
class Whatsapp(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(255), nullable=False)
    
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    confirm_password = db.Column(db.String(200))
    birthday = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    created_at = db.Column(db.DateTime)

class LoggedInUsers(db.Model):
    __tablename__ = 'logged_in_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    login_time = db.Column(db.DateTime)
    logout_time = db.Column(db.DateTime)
    is_logged_in = db.Column(db.Boolean, default=False)