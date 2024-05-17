import mysql.connector
from mysql.connector import Error
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    SFSUEmailVerified = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.UserID

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="12345678",
            database="FromHereToThere"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
