from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField

class InfoForm(FlaskForm):
    content = TextAreaField('content')
    image = FileField('image')
    submit = SubmitField('Submit')