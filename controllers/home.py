from flask import *
from extensions import db
import os

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/', methods=['GET'])
def home_route():
	if 'username' not in session:
		return redirect(url_for("home.login_route"))

	else:
		return render_template("base.html")

@home.route('/login', methods=['GET'])
def login_route():
	return render_template("login.html")

@home.route('/create-account', methods=['GET'])
def create_route():
	return render_template("createAccount.html")