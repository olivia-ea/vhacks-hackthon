
from flask import Flask, request, redirect, render_template, flash, session, jsonify, json, url_for
# from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
# import requests
# from model import 


app = Flask(__name__)
app.jinja_env.undefinded = StrictUndefined
app.debug = True