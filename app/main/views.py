from flask import render_template
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

@main.route('/register')
def register():
    form = RegForm()
    return render_template('main/register.html',title='register', form=form)

@main.route('/login')
def login():
    form = LoginForm()
    return render_template('main/login.html',title='login', form=form)




