from flask import Blueprint, render_template
from db_connection import get_db_connection

recent_items = Blueprint('recent_items', __name__, static_folder='./public', template_folder='./html')

@recent_items.route('/recentItemsPost')
def recent_items_post():
    # Connect to the database
    mydb = get_db_connection()
    cur = mydb.cursor(dictionary=True)

    # SQL query to select top 4 items sorted by PostDate
    query = "SELECT ItemName, file_name, PostDate FROM Listing ORDER BY PostDate DESC LIMIT 4"
    cur.execute(query)

    # Fetch data
    items = cur.fetchall()

    # Close cursor and database connection
    cur.close()
    mydb.close()

    # Render the recent items to the response HTML
    return render_template('pages/RecentItemResponse.html', items=items)
