from werkzeug.security import generate_password_hash
from db_connection import db, User
from flask import Flask
import logging

# Initialize Flask app and database (assuming you have a db connection setup in db_connection)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:newpassword@localhost/FromHereToThere'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def hash_plaintext_passwords():
    with app.app_context():
        users = User.query.all()
        for user in users:
            logging.debug(f"Processing user: {user.UserName}")
            if not user.Password.startswith('$2b$'):
                logging.debug(f"Hashing password for user: {user.UserName}")
                hashed_password = generate_password_hash(user.Password)
                user.Password = hashed_password
                db.session.commit()
                logging.info(f"Updated password for user {user.UserName}")
            else:
                logging.debug(f"Password for user {user.UserName} is already hashed")

if __name__ == "__main__":
    hash_plaintext_passwords()
