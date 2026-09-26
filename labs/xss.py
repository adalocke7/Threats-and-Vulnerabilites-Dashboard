from flask import render_template, Blueprint, request
from data import catalog_by_slug

xss_bp = Blueprint('xss', __name__, url_prefix='/xss')

@xss_bp.route('/', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        name = catalog_by_slug.get('xss', 'Cross-Site Scripting')
        return render_template('lab.html', item=name)