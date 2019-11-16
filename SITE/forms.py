from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class ExtendForm(FlaskForm):
    url = StringField("url",validators=[DataRequired(),URL()])
    submit = SubmitField("expand")