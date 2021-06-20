from flask import render_template, url_for
from . import main
from flask_login import login_required
from .. import db
# , bcrypt

# from forms import RegForm, LoginForm


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
# @login_required
def index():
    return render_template('index.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html',title='about')

