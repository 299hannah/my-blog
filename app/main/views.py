from ..models import User, Post
from flask import render_template, url_for, flash, redirect,abort,request
from . import main
from flask_login import login_required,current_user,login_user,logout_user
from .. import db
# , bcrypt

from .forms import RegForm, LoginForm


posts = [
    {
        'author':'Hannah',
        'title':'Blog 1',
        'content':'First post content',
        'date_posted':'April 20'
    },
    {
        'author':'Jane',
        'title':'Blog 2',
        'content':'second post content',
        'date_posted':'April 21'
    }
]

@main.route('/')
def index():
    return render_template('main/index.html', posts=posts)

@main.route('/about')
def about():
    return render_template('main/about.html',title='about')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
 

        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
        # user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # db.session.add(user)
        # db.session.commit()
        flash(f'Your account created you are now able to log in {form.username.data}!', 'primary')
        return redirect(url_for('main.login'))
    return render_template('main/register.html',title='register', form=form)

@main.route('/login', methods=['GET', 'POST'])
@login_required
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
          user = User.query.filter_by(email = form.email.data).first()
          if user is not None and user.verify_password(form.password.data):
            login_user(user,rememberMe=form.remember.data)
            return redirect(url_for('main.index'))
          else:
            flash('Log in unsuccessful please check your email or password', 'danger')

    return render_template('main/login.html',title='login', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))

