from flask import Blueprint, render_template, request, jsonify
import mysql.connector

search = Blueprint('search', __name__, static_folder='./public', template_folder='./html')

def get_db_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "admin",
        password = "12345678",
        database = "VerticalPrototype"
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
    product = []
    numrows = 0

    if request.method == 'POST':
        search_word = request.form['query']
        print("Received search query:", search_word)
        if search_word == '':
            query = "SELECT * from Product"
            cur.execute(query)
        else:
            query = "SELECT * from Product WHERE Title LIKE %s"
            cur.execute(query, ('%' + search_word + '%',))
        product = cur.fetchall()
        numrows = len(product)
    # Always close cursor and connection when done
    cur.close()
    mydb.close()
#    return render_template('about/response.html', product=product, numrows=numrows)
    return jsonify({'htmlresponse': render_template('about/response.html', product=product, numrows=numrows)})
