from flask import Blueprint, request, redirect, url_for, session
from FromHereToThereDB import get_FromHereToThereDB

login_bp = Blueprint('login_bp', __name__)

# Connect to the database
mydb = get_FromHereToThereDB()
cur = mydb.cursor(dictionary=True)

@login_bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Query the database to check if the user exists and credentials are correct
    query = "SELECT * FROM Users WHERE UserEmail = %s AND UserPassword = %s"
    cur.execute(query, (email, password))
    user = cur.fetchone()

    if user:
        # User exists and credentials are correct, set session variable to indicate user is logged in
        session['user_id'] = user['UserID']
        # Redirect the user to the dashboard or any other desired page
        return redirect(url_for('dashboard'))
    else:
        # User does not exist or credentials are incorrect, render the login page again with an error message
        return redirect(url_for('index'))  # Redirect to the login page with an error message

# Example of a route for the dashboard page
@login_bp.route('/dashboard')
def dashboard():
    # Check if the user is logged in by checking if the user_id is in the session
    if 'user_id' in session:
        # User is logged in, render the dashboard template
        return render_template('dashboard.html')
    else:
        # User is not logged in, redirect to the login page
        return redirect(url_for('index'))
