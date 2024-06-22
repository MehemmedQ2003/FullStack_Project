from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class WhatsappForm(FlaskForm):
    name = StringField('Name')
    number = StringField('Number')
    submit = SubmitField('Submit')