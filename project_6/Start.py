#!/usr/bin/env python

"""
应用启动类
"""



from flask import Flask,render_template,flash,url_for,redirect,Blueprint,session
from flask_bootstrap import Bootstrap

from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required
from flask_sqlalchemy import SQLAlchemy
import sys
import os
#解决flash的一个bug
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

#各项插件的配置
app.config['SECRET_KEY']='kkk'
#配置数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'user') 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap(app)

moment=Moment(app)

app.secret_key = 's3cr3t'
login_manger=LoginManager()
login_manger.session_protection='strong'
login_manger.login_view='pj6.login'
login_manger.init_app(app)

#session.permanent = True
#app.permanent_session_lifetime = timedelta(minutes=5)



@login_manger.user_loader
def load_user(user_id):
    from Model import Users
    return Users.query.get(int(user_id))

"""
蓝图注册
"""
def init():
    from Views import pj6
    app.register_blueprint(blueprint=pj6,url_prefix='/pj6')


if __name__ == '__main__':
    init()
    app.run(host="0.0.0.0",port=8002,debug=True)
