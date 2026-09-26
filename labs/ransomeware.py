from flask import render_template, Blueprint, request

ransomware_bp = Blueprint('ransomware', __name__, url_prefix='/ransomware')

@ransomware_bp.route('/', methods=['GET', 'POST'])
def ransomware():
    if request.method == 'POST':
        return render_template('lab.html', item={"name": "Ransomware"})