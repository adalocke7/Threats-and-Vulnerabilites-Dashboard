from flask import render_template, Blueprint, request

xss_bp = Blueprint('xss', __name__, url_prefix='/xss')

@xss_bp.route('/', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        return render_template('lab.html', item={"name": "Cross-Site Scripting"})