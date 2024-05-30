
from flask import *
import request
from models import bloomerUser

auth = Blueprint('auth', __name__)


@auth.route('/login_page', methods=['GET', 'POST'])
def login_page():
    message = 'default text'
    if request.method == "POST" and 'userEmail' in request.form and 'userPassword' in request.form:
        email = request.form['userEmail']
        password = request.form['userPassword']
        cu
    return render_template('login_page.html')
