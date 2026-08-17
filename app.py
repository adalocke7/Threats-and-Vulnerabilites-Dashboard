from flask import Flask, render_template
from data import catalog

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', catalog=catalog)

@app.route('/lab/sqli')
def lab():
    return render_template('lab.html', catalog=catalog)

@app.route('/lab/xss')
def lab():
    return render_template('lab.html', catalog=catalog)

@app.route('/lab/ransomware')
def lab():
    return render_template('lab.html', catalog=catalog)

@app.route('/lab/defaultcreds')
def lab():
    return render_template('lab.html', catalog=catalog)

if __name__ == '__main__':
    app.run(debug=True)