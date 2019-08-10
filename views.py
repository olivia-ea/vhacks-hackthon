
from flask import Flask, request, redirect, render_template, flash, session, jsonify, json, url_for
# from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
# import requests
# from model import 
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


app.jinja_env.undefinded = StrictUndefined
app.debug = True


@app.route('/')
def index():
    """ Homepage """

    return render_template('homepage.html')

@app.route('/login-page', methods=["GET"])
def returning_user_login():

    return render_template("login-page.html")

@app.route('/login-verification', methods=["POST"])
def returning_user_verification():

    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter(User.user_id==username).first()

    if user:
        if user.password == password:
            user_id = user.user_id
            session['logged_user'] = {'username': username}
            return render_template("dashboard.html")
        else:
            return("The password is incorrect.")
    else:
        return render_template('homepage.html')

    return render_template('returning_user.html')


@app.route('/register-new-user', methods=['GET'])
def register_new_user():

    return render_template('register_new_user.html')


@app.route('/new-user-login', methods=['POST'])
def process_new_user():

    user = User.query.filter(User.user_id==username).first()

    if user:
        flash("That username is already taken!")
    else:
        new_user = User(user_id=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        user_id = new_user.user_id
        session['logged_user'] = {'username': username}

        return render_template("dashboard.html")

    return render_template('new_user.html')


@app.route('/logout')
def logout():

    session.clear()
    # flash("Logged Out.")

    return redirect("/")


# flask_cors.CORS(app, expose_headers='Authorization')










