from flask import Blueprint, render_template, request, jsonify
import mysql.connector
from db_connection import get_db_connection


search = Blueprint('search', __name__, static_folder='./public', template_folder='./html')


#test db connection
#testdb = get_db_connection()
#testcur = testdb.cursor()
#testcur.execute('SELECT * FROM Product')

#product = testcur.fetchall()

#for Product in product:
#    print(Product)

@search.route('/pages/Search.html')
def search_page():
    return render_template('pages/Search.html')

#endpoint for search
@search.route("/ajaxlivesearch",methods=['GET'])
def ajaxlivesearch():
    mydb = get_db_connection()
    cur = mydb.cursor(dictionary=True)
    item = []
    numrows = 0

    if request.method == 'GET':
        search_word = request.args.get('query', '').strip()  # Remove trailing whitespace
        search_category = request.args.get('category','default')
        print("Received search query:", search_word)

        if search_word:
            if search_category in ['default', '']:
                query = "SELECT * FROM Listing WHERE ItemName LIKE %s"
                cur.execute(query, ('%' + search_word + '%',))
            else:
                query = "SELECT * FROM Listing WHERE ItemName LIKE %s AND Category = %s"
                cur.execute(query, ('%' + search_word + '%', search_category))
        else:
            if search_category in ['default', '']:
                # If no search word and default category, retrieve all listings
                query = "SELECT * FROM Listing"
                cur.execute(query)
            else:
                # If no search word but specific category selected, filter by category
                query = "SELECT * FROM Listing WHERE Category = %s"
                cur.execute(query, (search_category,))

        item = cur.fetchall()
        numrows = len(item)
        print("SQL Query: ", query)
        print("Formatted search word: ", search_word)
        print("Search results: ", item)
        print("Number of items found: ", numrows)
    # Always close cursor and connection when done
    cur.close()
    mydb.close()
    return jsonify({'htmlresponse': render_template('pages/response.html', item=item, numrows=numrows)})
