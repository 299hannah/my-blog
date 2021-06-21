from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.fields.simple import FileField
from wtforms.validators import Required, Email, EqualTo, email
from ..models import User
from flask_login import current_user
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed


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


class UpdateForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    picture = FileField('update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    
    def validate_email(self,email):
        if email.data != current_user.email:

            user= User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Email already exists')

    def validate_username(self,username):
        if username.data != current_user.username:

            user= User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Username is not available')





