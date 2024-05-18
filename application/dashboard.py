from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from db_connection import get_db_connection

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='./public/html')

@dashboard_bp.route('/userListings', methods=['GET'])
@login_required
def user_listings():
    try:
        mydb = get_db_connection()
        cur = mydb.cursor(dictionary=True)
        query = """
            SELECT 
                Listing.ItemName, 
                Listing.PhotoName AS file_name, 
                Listing.Description,
                Listing.Price,
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
        cur.execute(query, (current_user.UserID,))
        listings = cur.fetchall()
        cur.close()
        mydb.close()
        return jsonify({'listings': listings})
    except Exception as e:
        print("Error occurred:", e)
        return jsonify({'error': str(e)}), 500
