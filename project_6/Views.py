#!/usr/bin/env python

"""
视图模型
"""

from flask import render_template,Blueprint,redirect,url_for,flash,session
from Start import login_manger
from Form import Login_Form,Register_Form
from Model import  Users
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required
from Start import db
import psutil

pj6=Blueprint('pj6',__name__)  #蓝图


@pj6.route('/login')
def index():
    form=Login_Form()
    return render_template('login.html',form=form)

@pj6.route('/index')
def l_index():
    form = Login_Form()
    return render_template('login.html',form=form)

	
'''
@pj6.route('/login',methods=['GET','POST'])
def login():
	form=Login_Form()
	if form.validate_on_submit():
		user=Users.query.filter_by(name=form.name.data).first()
		if user is not  None and user.pwd==form.pwd.data:
			login_user(user)
			flash('登录成功')
			totalram=psutil.virtual_memory().total/1024/1024
			usedram=psutil.virtual_memory().used/1024/1024
			cpu=psutil.cpu_percent()
			return  render_template('ok.html',total_ram=totalram,used_ram=usedram,cpu=cpu)
		else:
			if user is None:
				flash('用户名错误')
				#return render_template('login.html',form=form)
			else:
				flash('密码错误')
				#return render_template('login.html',form=form)
	return render_template('login.html',form=form)
'''
@pj6.route('/login',methods=['GET','POST'])
def login():
	form=Login_Form()
	if form.validate_on_submit():
		user=Users.query.filter_by(name=form.name.data).first()
		if user is None:
			flash('Wrong username')
			return render_template('login.html',form=form)
		if user is not  None and user.pwd!=form.pwd.data:
			flash('Wrong password')
			return render_template('login.html',form=form)
		if user is not  None and user.pwd==form.pwd.data:
			login_user(user)
			flash('Log in succeed')
			return  redirect(url_for('pj6.ok'))
	#return render_template('login.html',form=form)
@pj6.route('/ok')
@login_required
def ok():
	totalram=psutil.virtual_memory().total/1024/1024
	usedram=psutil.virtual_memory().used/1024/1024
	cpu=psutil.cpu_percent()
	return  render_template('ok.html',total_ram=totalram,used_ram=usedram,cpu=cpu)


#用户登出
@pj6.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Loged out')
    return redirect(url_for('pj6.index'))


@pj6.route('/register',methods=['GET','POST'])
def register():
	form=Register_Form()
	if form.validate_on_submit():
		user=Users.query.filter_by(name=form.name.data).first()
		if user is not None and user.name==form.name.data:
			flash('User already exist')
			return redirect(url_for('pj6.register'))
		else:
			user=Users(name=form.name.data,pwd=form.pwd.data)
			db.session.add(user)
			db.session.commit()
			flash('Register succeed')
			return redirect(url_for('pj6.index'))
	return render_template('register.html',form=form)




