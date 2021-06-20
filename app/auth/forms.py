from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class RegForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password',validators = [Required(),EqualTo('confirmPassword',message = 'Password must match')])
    confirmPassword = PasswordField('ConfirmPassword', validators=[Required()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email already exists')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username is not available')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    rememberMe = BooleanField('RememberMe')
    submit = SubmitField('Login')




