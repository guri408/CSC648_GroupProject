from flask import Blueprint, render_template, request, jsonify
import mysql.connector

search = Blueprint('search', __name__, static_folder='./public', template_folder='./html')

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "12345678",
    database = "VerticalPrototype"
    )

@search.route('/about/Search.html')
def search_page():
    return render_template('about/Search.html')

@search.route("/ajaxlivesearch", methods= ["POST", "GET"'])
def ajaxlivesearch():
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)

    return jsonify('success')


#@search.route("/ajaxlivesearch",methods=["POST","GET"])
#def ajaxlivesearch():
#    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#    if request.method == 'POST':
#        search_word = request.form['query']
#        print(search_word)
#        if search_word == '':
#            query = "SELECT * from Product ORDER BY id"
#            cur.execute(query)
#            product = cur.fetchall()
#        else:
#            query = "SELECT * from Product WHERE Title LIKE '%{}%' ORDERED BY id".format(search_word,search_word,search_word)
#            cur.execute(query)
#            numrows = int(cur.rowcount)
#            product = cur.fetchall()
#            print(numrows)
#    return jsonify({'htmlresponse': render_template('about/response.html', product=product, numrows=numrows)})
