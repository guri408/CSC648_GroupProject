from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from db_connection import get_db_connection, User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

login_bp = Blueprint('login_bp', __name__)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login_bp.dashboard'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(Email=email).first()
        if user and check_password_hash(user.Password, password):
            login_user(user)
            return redirect(url_for('login_bp.dashboard'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('Login.html', form=form)

@login_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('Dashboard.html', user=current_user)

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_bp.login'))
