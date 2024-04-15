from flask import Blueprint, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from db_connection import get_db_connection  # Use the shared database connection function
import mysql.connector

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/submit_item', methods=['POST'])
def submit_item():
    conn = get_db_connection()
    if not conn:
        return 'Database connection failed', 500

    item_name = request.form['itemName']
    item_price = request.form['itemPrice']
    category = request.form['category']
    item_desc = request.form.get('itemDesc', '')
    item_pic = request.files['itemPic']

    if item_pic and item_pic.filename != '':
        filename = secure_filename(item_pic.filename)
        file_path = os.path.join('/var/www/csc648-sp24-03-team03/application/public/Product_Images', filename)
        item_pic.save(file_path)

        cursor = conn.cursor()
        sql = "INSERT INTO Listing (ItemName, ItemDescription, Category, Price, file_name, file_path) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (item_name, item_desc, category, item_price, filename, file_path))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))  # Redirect to the index after insertion

    return 'Failed to upload file', 400
