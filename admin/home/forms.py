from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField

class HomeForm(FlaskForm):
    title = StringField('Title')
    image = FileField('Image')
    description = StringField('description')
    submit = SubmitField('Submit')