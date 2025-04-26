from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length , ValidationError
from models.auth import User

def validate_username(form , field):
    new_user = User.query.filter_by(username=field.data).first()
    if new_user:
        raise ValidationError('Username is taken')

def validate_phone_number(form , field):
    new_user = User.query.filter_by(phone_number = field.data).first()
    if new_user:
        raise ValidationError("Phone number is taken")


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=3, max=30) , validate_username
    ])
    email = StringField('Email Address', validators=[
        DataRequired(), Email()
    ])
    phone_number = StringField('Phone Number', validators=[
        DataRequired(), Length(min=8, max=20) , validate_phone_number
    ])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6)
    ])
    submit = SubmitField('Sign Up')




class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')



