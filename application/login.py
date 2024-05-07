from flask import Blueprint, render_template, jsonify
from db_connection import get_db_connection

login = Blueprint('login', __name__, static_folder='./public', template_folder='./public/html')

@login.route('/Login.html')
def login_page():
    return render_template('/Login.html')
