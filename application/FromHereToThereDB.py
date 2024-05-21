# FromHereToThereDB
import mysql.connector
from mysql.connector import Error

def get_FromHereToThereDB():
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