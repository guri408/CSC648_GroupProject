from flask import Blueprint, render_template, request, jsonify
import mysql.connector

search = Blueprint('search', __name__, static_folder='./public', template_folder='./html')

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "12345678",
    database = "VerticalPrototype"
    )

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM Product')

product = mycursor.fetchall()

for Product in product:
    print(Product)

@search.route('/about/Search.html')
def search_page():
    return render_template('about/Search.html')

@search.route("/ajaxlivesearch", methods=["POST", "GET"])
def ajaxlivesearch():
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
    return jsonify('success')



#@search.route("/ajaxlivesearch", methods=["POST", "GET"])
#def ajaxlivesearch():
#    cur = mydb.cursor()
#    if request.method == 'POST':
#        search_word = request.form['query']
#        print(search_word)  # Print for debugging
#        if search_word != '':
#            query = "SELECT * FROM PRODUCT WHERE Title LIKE %s"
#            # Use parameterized query to prevent SQL injection
#            cur.execute(query, ('%' + search_word + '%',))
#            product = cur.fetchall()
#        else#:
#            product = []  # Return empty list if search term is empty

#        return jsonify({'htmlresponse': render_template('about/response.html', product=product)})
#    else:
#        return jsonify({'error': 'Invalid request method'})

