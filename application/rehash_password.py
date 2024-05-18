from werkzeug.security import generate_password_hash
from db_connection import db, User
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:newpassword@localhost/FromHereToThere'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    user = User.query.filter_by(Email='Test1@mail.sfsu.edu').first()
    if user:
        user.Password = generate_password_hash('12345678')
        db.session.commit()
        print(f"Updated password for user {user.UserName}")
    else:
        print("User not found")
