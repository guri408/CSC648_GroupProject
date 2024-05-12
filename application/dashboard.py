from flask import Blueprint, render_template, request
from db_connection import get_db_connection

dashboard = Blueprint('dashboard', __name__, static_folder='./public', template_folder='./public/html')

@dashboard.route('/Dashboard.html')
def dashboard_page():
    return render_template('/Dashboard.html')
