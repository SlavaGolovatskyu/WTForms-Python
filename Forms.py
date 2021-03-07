from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

""" 
	Пакет wtform предлагает несколько классов, представляющих собой следующие поля:
	StringField, PasswordField, SelectField, TextAreaField, SubmitField
"""

class ContactForm(FlaskForm):
	name = StringField("Name: ", validators=[DataRequired()])
	email = StringField("Email: ", validators=[Email()])
	message = TextAreaField("Message", validators=[DataRequired()])
	submit = SubmitField("Submit")

