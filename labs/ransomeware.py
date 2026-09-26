from flask import render_template, Blueprint, request
from data import catalog

ransomware_bp = Blueprint('ransomware', __name__, url_prefix='/ransomware')

@ransomware_bp.route('/', methods=['GET', 'POST'])
def ransomware():
    if request.method == 'POST':
        name = catalog_by_slug.get('ransomware', 'Ransomware')
        return render_template('lab.html', item=name)