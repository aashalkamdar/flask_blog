from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired(),Length(min=2,max=20)])

	email = StringField('Email',
		validators = [DataRequired(),Email()])

	password = PasswordField('Password',
		validators=[DataRequired()])

	confirm_password = PasswordField('Confirm Password', 
		validators = [DataRequired(), EqualTo('password')])


	submit = SubmitField('Sign up')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username already exists, please choose another username.')

	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError('Email already exists, please choose another email.')



class LoginForm(FlaskForm):

	email = StringField('Email',
		validators = [DataRequired(),Email()])

	password = PasswordField('Password',
		validators=[DataRequired()])

	remember = BooleanField('remember me')

	#remember allows users to be logged in after they close window
	#using secure cookie


	submit = SubmitField('login')


class UpdateAccountForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired(),Length(min=2,max=20)])

	email = StringField('Email',
		validators = [DataRequired(),Email()])

	picture = FileField('Update Profile Picture',
		validators=[FileAllowed(['jpg', 'png','jpeg'])])

	submit = SubmitField('Update')

	def validate_username(self,username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Username already exists, please choose another username.')

	def validate_email(self,email):
		if email.data != current_user.email:

			user = User.query.filter_by(email=email.data).first()

			if user:
				raise ValidationError('Email already exists, please choose another email.')


class RequestResetForm(FlaskForm):
	email = StringField('Email',
	validators = [DataRequired(),Email()])

	submit = SubmitField('Request Password Reset')

	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()

		if user is None:
			raise ValidationError('Thre is no account with that email, you must register first')

class ResetPasswordForm(FlaskForm):

	password = PasswordField('Password',
		validators=[DataRequired()])

	confirm_password = PasswordField('Confirm Password', 
		validators = [DataRequired(), EqualTo('password')])

	submit = SubmitField('Password Reset')
