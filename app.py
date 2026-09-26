from flask import Flask, render_template, Blueprint, request
from data import catalog
from labs.sqli import sqli_bp
from labs.xss import xss_bp
from labs.ransomeware import ransomware_bp
from labs.default_creds import defaultcreds_bp

app = Flask(__name__)

app.register_blueprint(sqli_bp)
app.register_blueprint(xss_bp)
app.register_blueprint(ransomware_bp)
app.register_blueprint(defaultcreds_bp)

@app.route('/')
def home():
    return render_template('home.html', catalog=catalog)


if __name__ == '__main__':
    app.run(debug=True)