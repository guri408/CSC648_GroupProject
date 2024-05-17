import pymysql
pymysql.install_as_MySQLdb()

# Your existing imports
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from flask_wtf.csrf import CSRFProtect
import logging
from db_connection import db, User, get_db_connection
from search import search_bp
from item_submission import item_bp
from login import login_bp
from signup import signup_bp
from compose import compose
from recent_items import recent_items
from flask_login import LoginManager

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_folder='./public', template_folder='./public/html')

# Configuration settings
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/FromHereToThere'
db.init_app(app)

# Initialize extensions
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_bp.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define the signup form
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[
        DataRequired(), Email(), Regexp(r'.*@(mail\.sfsu\.edu|sfsu\.edu)$', message="Must be a valid SFSU email")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=8, message="Password must be at least 8 characters long")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message="Passwords must match")
    ])
    agree_tos = BooleanField('I agree to the Terms of Service', validators=[DataRequired()])
    submit = SubmitField('Signup')

# Register Blueprints
app.register_blueprint(search_bp, url_prefix="")
app.register_blueprint(item_bp, url_prefix="")
app.register_blueprint(recent_items, url_prefix="")
app.register_blueprint(login_bp, url_prefix="")
app.register_blueprint(signup_bp, url_prefix="")
app.register_blueprint(compose, url_prefix="")

# Define routes
@app.route('/Index.html')
@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/about')
def about():
    return render_template('about/About.html')

@app.route('/about/Justin.html')
def justin():
    return render_template('about/Justin.html')

@app.route('/about/Douglas.html')
def douglas():
    return render_template('about/Douglas.html')

@app.route('/about/GioJung.html')
def giojung():
    return render_template('about/GioJung.html')

@app.route('/about/Gurpreet.html')
def gurpreet():
    return render_template('about/Gurpreet.html')

@app.route('/about/Gursimran.html')
def gursimran():
    return render_template('about/Gursimran.html')

@app.route('/about/Omar.html')
def omar():
    return render_template('about/Omar.html')

@app.route('/Sell.html')
def sell():
    return render_template('/Sell.html')

@app.route('/Search.html')
def search_page():
    return render_template('/Search.html')

@app.route('/Signup.html', methods=['GET', 'POST'])
def signup_page():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                try:
                    # Check if the email or username already exists
                    cursor.execute("SELECT * FROM User WHERE Email = %s OR UserName = %s", (email, username))
                    existing_user = cursor.fetchone()

                    if existing_user:
                        flash('An account with this email or username already exists.', 'danger')
                    else:
                        cursor.execute(
                            "INSERT INTO User (UserName, Email, Password) VALUES (%s, %s, %s)",
                            (username, email, hashed_password)
                        )
                        conn.commit()
                        flash('Your account has been created!', 'success')
                        return redirect(url_for('login_bp.login'))
                except Error as err:
                    logging.error(f"Database error: {err}")
                    flash(f"Database error: {err}", 'danger')
                finally:
                    cursor.fetchall()  # Ensure all results are read
                    cursor.close()
                    conn.close()
            else:
                flash('Database connection failed', 'danger')
        except Exception as e:
            logging.error(f"Error: {e}")
            flash(f"Error: {e}", 'danger')
    else:
        # Debugging: Print form validation errors
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                logging.debug(f"Error in {fieldName}: {err}")
                flash(f"Error in {fieldName}: {err}", 'danger')
    return render_template('Signup.html', form=form)

@app.route('/Login.html')
def login_page():
    return render_template('Login.html')

@app.route('/Dashboard.html')
def dashboard_page():
    return render_template('Dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

