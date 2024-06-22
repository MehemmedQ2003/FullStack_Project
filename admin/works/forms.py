from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, TextAreaField

class WorksForm(FlaskForm):
    title = StringField('Title')
    image = FileField('image')
    detail = TextAreaField('Detail')
    submit = SubmitField('Submit')