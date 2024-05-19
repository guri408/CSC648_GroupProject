from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from db_connection import get_db_connection
import logging

logging.basicConfig(level=logging.DEBUG)

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='./public/html')

@dashboard_bp.route('/userListings', methods=['GET'])
@login_required
def user_listings():
    try:
        mydb = get_db_connection()
        cur = mydb.cursor(dictionary=True)
        logging.debug('Database connection established.')
        
        query = """
            SELECT 
                Listing.*, 
                Category.CategoryName 
            FROM 
                Listing 
            JOIN 
                Category 
            ON 
                Listing.CategoryID = Category.CategoryID 
            WHERE 
                Listing.UserID = %s
        """
        logging.debug('Executing query: %s', query)
        cur.execute(query, (current_user.UserID,))
        listings = cur.fetchall()
        logging.debug('Query executed successfully. Listings: %s', listings)
        
        cur.close()
        mydb.close()
        logging.debug('Database connection closed.')
        
        return jsonify({'listings': listings})
    except Exception as e:
        logging.error("Error occurred:", exc_info=True)
        return jsonify({'error': str(e)}), 500
