from flask import Flask, render_template

app = Flask(__name__, static_folder='./css', template_folder='./html')

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/index.html')
#def index():
#    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about/About.html')

@app.route('/about/Justin')
def justin():
    return render_template('about/Justin.html')

@app.route('/about/Douglas')
def douglas():
    return render_template('about/Douglas.html')

@app.route('/about/GioJung')
def giojung():
    return render_template('about/GioJung.html')

@app.route('/about/Gurpreet')
def gurpreet():
    return render_template('about/Gurpreet.html')

@app.route('/about/Gursimran')
def gursimran():
    return render_template('about/Gursimran.html')

@app.route('/about/Omar')
def omar():
    return render_template('about/Omar.html')

if __name__ == '__main__':
    app.run(debug=True)
