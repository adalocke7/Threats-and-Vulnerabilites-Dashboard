from flask import render_template, Blueprint, request
from data import catalog_by_slug

sqli_bp = Blueprint('sqli', __name__, url_prefix='/sqli')

@sqli_bp.route('/', methods=['GET', 'POST'])
def sqli():
    if request.method == 'POST':
        name = catalog_by_slug.get('sqli', 'SQL Injection')
        return render_template('lab.html', item=name)
