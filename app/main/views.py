from flask import render_template, url_for, flash, redirect
from . import main
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
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'primary')
        return redirect(url_for('main.index'))
    return render_template('main/register.html',title='register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'myblog@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'primary')
            return redirect(url_for('main.index'))

        else:
            flash('Log in unsuccessful please check your username or password', 'danger')

    return render_template('main/login.html',title='login', form=form)




