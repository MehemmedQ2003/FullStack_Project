from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField

class ContactForm(FlaskForm):
    country = StringField('Country')
    city = StringField('City')
    title = StringField('Title')
    address = StringField('Address')
    address_link = StringField('Address Link')
    phone = StringField('Phone')
    email = StringField('Email')
    submit = SubmitField('Submit')