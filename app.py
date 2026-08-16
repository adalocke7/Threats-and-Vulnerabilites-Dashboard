from flask import Flask, render_template
from data import catalog

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', catalog=catalog)

if __name__ == '__main__':
    app.run(debug=True)