
from flask import Flask, request, redirect, render_template, flash, session, jsonify, json, url_for
# from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
# import requests
# from model import 

app = Flask(__name__)
app.jinja_env.undefinded = StrictUndefined
app.debug = True


@app.route('/')
def index():
    """ Homepage """

    # has description of what the app does
    # displays returning user or new user routes

    return render_template('homepage.html')

@app.route('/login-verification', methods=["GET"])
def returning_user_login():

    username = request.form.get("username")
    password = request.form.get("password")

    try:
        user = Seeking_Help_User.query.filter(Seeking_Help_User.user_id==username).first()
    except:
        pass

    try:
        user = Looking_To_Help_User.query.filter(Looking_To_Help_User.user_id==username).first()
    except:
        pass

    # how to handle if user has both accounts?

    if user:
        if user.password == password:
            user_id = user.user_id
            return redirect("dashboard.html")
        else:
            return("The password is incorrect.")
    else:
        return render_template('homepage.html')
        
    return render_template('returning_user.html')


@app.route('/new-user-login')
def new_user_login():

    # are you seeking help or looking to help => anchor to bottom to registration form

    return render_template('new_user.html')











