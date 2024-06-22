from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField

class TechnologiesForm(FlaskForm):
    title = StringField('Title')
    image = FileField('Image')
    content = TextAreaField('content')
    submit = SubmitField('Submit')