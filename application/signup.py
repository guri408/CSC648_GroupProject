from flask import Blueprint, request, redirect, url_for
import os
#from db_connection import get_db_connection  # Use the shared database connection function
from FromHereToThereDB import get_FromHereToThereDB
import mysql.connector


signup_bp = Blueprint('signup_bp', __name__)

@signup_bp.route('/signup_account', methods=['POST'])
def singup_account():
    conn = get_FromHereToThereDB()
    if not conn:
        return 'Database connection failed', 500

    UserEmail = request.form['UserEmail']
    UserPassword = request.form['UserPassword']

    if UserEmail.endswith('sfsu.edu'):
        cursor = conn.cursor()
        sql = "INSERT INTO User (Email, Password) values (%s, %s)"
        cursor.execute(sql, (UserEmail, UserPassword))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('Login')) #Redirect to the login page after signup

    return 'Failed to upload file', 400


