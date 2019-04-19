#!/usr/bin/env python

"""
表单类
"""

from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import  Required,Email,EqualTo
from flask_wtf import FlaskForm

#登录表单
class Login_Form(FlaskForm):
    name=StringField('Email address',validators=[Required(),Email()])
    pwd=PasswordField('password',validators=[Required()])
    submit=SubmitField('login in')


#注册表单
class Register_Form(FlaskForm):
    name=StringField('Email address',validators=[Required(),Email()])
    pwd=PasswordField('password',validators=[Required()])
    pwd_again=PasswordField('password again',validators=[Required(),EqualTo('pwd', message='Passwords must match')])
    submit=SubmitField('register')
class Ok(FlaskForm):
    pass
