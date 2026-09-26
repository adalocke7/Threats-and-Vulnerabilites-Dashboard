from flask import render_template, Blueprint, request

defaultcreds_bp = Blueprint('defaultcreds', __name__, url_prefix='/defaultcreds')

@defaultcreds_bp.route('/', methods=['GET', 'POST'])
def defaultcreds():
    if request.method == 'POST':   
        return render_template('lab.html', item={"name": "Default Credentials"})