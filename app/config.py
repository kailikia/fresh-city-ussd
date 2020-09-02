from flask import Flask, request, make_response, render_template,redirect,url_for,flash,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import random
import string
import re

# DB_URL = 'postgresql://postgres:123456@127.0.0.1:5432/freshcity_ussd'

DB_URL = 'postgresql://myuser:mypass@172.17.0.1:5432/freshcity_ussd'

app = Flask(__name__)
app.secret_key = 'Sc$4677*&E%9%d3DW2@#E465*&rc4e*3'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='some-secret-string'

db = SQLAlchemy(app)



