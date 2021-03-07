from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

"""  
	WTForms
	WTForms – это мощная библиотека, написанная на Python и независимая от фреймворков. Она умеет генерировать формы,
	проверять их и предварительно заполнять информацией (удобно для редактирования) и многое другое. 
	Также она предлагает защиту от CSRF. Для установки WTForms используется Flask-WTF.

	Flask- WTF – это расширение для Flask, которое интегрирует WTForms во Flask. Оно также предлагает дополнительные функции,
	такие как загрузка файлов, reCAPTCHA, интернационализация (i18n) и другие. Для установки Flask-WTF нужно ввести следующую команду
	
	
	Пакет wtform предлагает несколько классов, представляющих собой следующие поля:
	StringField, PasswordField, SelectField, TextAreaField, SubmitField
"""

class ContactForm(FlaskForm):
	name = StringField("Name: ", validators=[DataRequired()])
	email = StringField("Email: ", validators=[Email()])
	message = TextAreaField("Message", validators=[DataRequired()])
	submit = SubmitField("Submit")

