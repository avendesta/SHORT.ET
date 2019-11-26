from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, URL, Email, EqualTo, ValidationError
from short.models import User
from short.password_strength import weakness

class ExtendForm(FlaskForm):
    url = StringField("URL",validators=[DataRequired(),Length(min=2,max=50), URL()])
    submit = SubmitField("Expand")

class RegisterForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=40)])
    email = StringField('Email',
                        validators=[DataRequired(), Length(min=2,max=40), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=2,max=60)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), Length(min=2,max=60), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("username already exists!")

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("email already exists!")

    def validate_password(self,password):
        password = password.data
        if weakness(password)>1000:
            raise ValidationError("Password is very common, Try another one!")

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=2,max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2,max=60)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')