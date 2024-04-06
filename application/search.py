from flask import Blueprint, render_template, request, jsonify
import mysql.connector

search = Blueprint('search', __name__, static_folder='./public', template_folder='./html')

def get_db_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "admin",
        password = "12345678",
        database = "TestSearch"
    )

#test db connection
#testdb = get_db_connection()
#testcur = testdb.cursor()
#testcur.execute('SELECT * FROM Product')

#product = testcur.fetchall()

#for Product in product:
#    print(Product)

@search.route('/about/Search.html')
def search_page():
    return render_template('about/Search.html')

#endpoint for search
@search.route("/ajaxlivesearch",methods=['GET', 'POST'])
def ajaxlivesearch():
    mydb = get_db_connection()
    cur = mydb.cursor(dictionary=True)
    item = []
    numrows = 0

    if request.method == 'POST':
        search_word = request.form['query']
        print("Received search query:", search_word)
        if search_word == '':
            query = "SELECT * from Listing"
            cur.execute(query)
        else:
            query = "SELECT * from Listing WHERE ItemName LIKE %s"
            cur.execute(query, ('%' + search_word + '%',))
        item = cur.fetchall()
        numrows = len(item)
    # Always close cursor and connection when done
    cur.close()
    mydb.close()
    return jsonify({'htmlresponse': render_template('about/response.html', item=item, numrows=numrows)})


#
#@search.route("/ajaxlivesearch",methods=['GET', 'POST'])
#def ajaxlivesearch():
#    mydb = get_db_connection()
#    cur = mydb.cursor(dictionary=True)
#    item = []
#    numrows = 0
#
#    if request.method == 'POST':
#        search_word = request.form['query']
#        category = request.form.get('category')  # Get the category from the request
#        
#        print("Received search query:", search_word)
#        print("Received category:", category)
#        
#        # Build the SQL query based on whether a category is specified or not
#        if category:  # If a category is specified
#            query = "SELECT * FROM Listing WHERE ItemName LIKE %s AND Category = %s"
#            cur.execute(query, ('%' + search_word + '%', category))
#        else:  # If no category is specified
#            query = "SELECT * FROM Listing WHERE ItemName LIKE %s"
#            cur.execute(query, ('%' + search_word + '%',))
#
#        item = cur.fetchall()
#        numrows = len(item)
#    
#    # Always close cursor and connection when done
#    cur.close()
#    mydb.close()
#    
#    return jsonify({'htmlresponse': render_template('about/response.html', item=item, numrows=numrows)})
