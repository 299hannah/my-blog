import os
import secrets
from PIL import Image
from flask import  render_template,redirect,url_for,request,flash
from . import auth
from flask_login import login_required,current_user,login_user,logout_user
from .. import db
from .forms import RegForm,LoginForm,UpdateForm
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash(f'Your account created you are now able to log in {form.username.data}!', 'primary')
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


def save_picture(form_picture):
    #returns filename and extension itself
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('app/static/photos',picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)


    i.save(picture_path)

    return picture_fn



@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file  = picture_file

        current_user.username =form.username.data
        current_user.email =form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'primary')
        return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

            
    image_file = url_for('static', filename='photos/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)



