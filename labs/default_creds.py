from flask import render_template, Blueprint, request
from data import catalog_by_slug

defaultcreds_bp = Blueprint('defaultcreds', __name__, url_prefix='/defaultcreds')

@defaultcreds_bp.route('/', methods=['GET', 'POST'])
def defaultcreds():
    if request.method == 'POST':   
        name = catalog_by_slug.get('defaultcreds', 'Default Credentials')
        return render_template('lab.html', item=name)