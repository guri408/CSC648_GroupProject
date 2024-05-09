from flask import Blueprint, render_template, request
from db_connection import get_db_connection

signup = Blueprint('signup', __name__, static_folder='./public', template_folder='./public/html')

@signup.route('/Signup.html')
def singup_page():
    return render_template('/Signup.html')
