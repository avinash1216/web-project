from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_blog.models import User
from flask_login import current_user
from flask_wtf.file import FileField,FileAllowed


class RegistrationForm(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    confirm_password=PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username has been taken. Please choose another one")
    
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email has been taken. Please choose another one")

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('email',validators=[DataRequired(),Email()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    submit=SubmitField('Update')

    def validate_username(self,username):
        if current_user.username!=username.data:
            user=User.query.filter_by(username=username.data).first()
            if user:
                 raise ValidationError("That username has been taken. Please choose another one")
           
    
    def validate_email(self,email):
        if current_user.email!=email.data:
             user=User.query.filter_by(email=email.data).first()
             if user:
                 raise ValidationError("That email has been taken. Please choose another one")

class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])
    submit=SubmitField('POST')