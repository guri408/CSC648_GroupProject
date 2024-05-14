from flask import Blueprint, render_template, request, jsonify
from db_connection import get_db_connection

# Define the Blueprint
search_bp = Blueprint('search_bp', __name__, template_folder='./public/html')

@search_bp.route('/searchingPost', methods=['GET'])
def searching_post():
    query = request.args.get('query', '')
    category = request.args.get('category', '')
    price_range = request.args.get('price_range', 'None')
    rental_price_range = request.args.get('rental_price_range', 'None')
    
    # Connect to the database
    mydb = get_db_connection()
    cur = mydb.cursor(dictionary=True)
    
    # Construct the SQL query based on the inputs
    sql_query = """
        SELECT Listing.*, Category.CategoryName 
        FROM Listing 
        JOIN Category ON Listing.CategoryID = Category.CategoryID 
        WHERE ItemName LIKE %s
    """
    values = [f'%{query}%']
    
    if category and category != 'default':
        sql_query += " AND Category.CategoryName = %s"
        values.append(category)

    if price_range != 'None' or rental_price_range != 'None':
        sql_query += " ORDER BY"
        if price_range != 'None':
            sql_query += " Listing.Price" + (" ASC" if price_range == 'LowHigh' else " DESC")
        if price_range != 'None' and rental_price_range != 'None':
            sql_query += ","
        if rental_price_range != 'None':
            sql_query += " Listing.RentalPrice" + (" ASC" if rental_price_range == 'LowHigh' else " DESC")

    cur.execute(sql_query, values)
    results = cur.fetchall()
    cur.close()
    mydb.close()
    
    # Render the results into HTML
    htmlresponse = render_template('response.html', items=results)
    return jsonify({'htmlresponse': htmlresponse})
