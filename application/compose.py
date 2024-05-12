from flask import Blueprint, render_template, request
from db_connection import get_db_connection

compose = Blueprint('compose', __name__, static_folder='./public', template_folder='./public/html')

@compose.route('/Compose.html')
def compose_page():
    return render_template('/Compose.html')
