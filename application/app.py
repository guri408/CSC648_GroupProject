from flask import Flask, render_template, request, jsonify
from search import search
from item_submission import item_bp
from login import login
from signup import signup
from compose import compose
import mysql.connector
from db_connection import get_db_connection
from recent_items import recent_items

app = Flask(__name__, static_folder='./public', template_folder='./public/html')
#mysql = MySQL(app)

# Register the Blueprint with the app
app.register_blueprint(search, url_prefix="")
app.register_blueprint(item_bp, url_prefix="")
app.register_blueprint(recent_items, url_prefix="")
app.register_blueprint(login, url_prefix="")
app.register_blueprint(signup, url_prefix="")
app.register_blueprint(compose, url_prefix="")


@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about/About.html')

@app.route('/about/Justin.html')
def justin():
    return render_template('about/Justin.html')

@app.route('/about/Douglas.html')
def douglas():
    return render_template('about/Douglas.html')

@app.route('/about/GioJung.html')
def giojung():
    return render_template('about/GioJung.html')

@app.route('/about/Gurpreet.html')
def gurpreet():
    return render_template('about/Gurpreet.html')

@app.route('/about/Gursimran.html')
def gursimran():
    return render_template('about/Gursimran.html')

@app.route('/about/Omar.html')
def omar():
    return render_template('about/Omar.html')

@app.route('/Sell.html')
def sell():
    return render_template('/Sell.html')
@app.route('/Search.html')
def search_page():
    return render_template('/Search.html')

#@app.route('/Login.html')
#def login_page():
#    return render_template('/Login.html')

if __name__ == '__main__':
    app.run(debug=True)
