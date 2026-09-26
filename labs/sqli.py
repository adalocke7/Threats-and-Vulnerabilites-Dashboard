from flask import render_template, Blueprint, request

sqli_bp = Blueprint('sqli', __name__, url_prefix='/sqli')

@sqli_bp.route('/', methods=['GET', 'POST'])
def sqli():
    if request.method == 'POST':
        return render_template('lab.html', item={"name": "SQL Injection"})
