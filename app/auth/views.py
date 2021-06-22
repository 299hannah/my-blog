from flask import  render_template,redirect,url_for,request,flash,abort
from . import auth
from flask_login import current_user,login_user,logout_user
from .. import db
from .forms import RegForm,LoginForm
from ..models import User
from ..email import mail_message

@auth.route('/register', methods=['GET', 'POST'])
def register():
   
    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Myblog", "welcome_user",user.email,user=user)

        # flash(f'Your account created you are now able to log in {form.username.data}!', 'primary')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',title='register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
# @login_required
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
          user = User.query.filter_by(email = form.email.data).first()
          if user is not None and user.verify_password(form.password.data):
            login_user(user,form.rememberMe.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
          else:
            flash('Log in unsuccessful please check your email or password', 'danger')

    return render_template('auth/login.html',title='login', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))

