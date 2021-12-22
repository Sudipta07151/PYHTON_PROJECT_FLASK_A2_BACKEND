from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(2, 45)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(5, 15)])
    confirm_password = PasswordField('ConfirmPassword', validators=[
        DataRequired(), Length(5, 15), EqualTo('password')])
    submit = SubmitField('Sign Up')


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(5, 15)])
    submit = SubmitField('Login')
