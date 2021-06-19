from flask import render_template
from . import main

@main.errorhandler(404)
def four_Ow_four(error):
    '''
    404 error page
    '''
    return render_template('fourOwfour.html'),404