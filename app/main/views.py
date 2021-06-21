
from flask import render_template
from . import main
from flask_login import login_required
# posts = [
#     {
#         'author': 'Manada Butate',
#         'title': 'New Blog',
#         'content': 'Mambo Vipi',
#         'date_posted': 'April 12, 2021'
        
#     },
#     {
#         'author': 'Tika Ingoha',
#         'title': 'Trending Blod',
#         'content': 'Haba na Haba',
#         'date_posted': 'April 21, 2021'
        
#     }
# ]
@main.route('/')
# @login_required
def home():
    return render_template('index.html')
@main.route('/about')
def about():
    return render_template('about.html', title = 'About')
