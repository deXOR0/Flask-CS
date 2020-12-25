from flask import render_template, url_for, redirect, flash
from app_name import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
# Uncomment the two lines below to implement Model and Form
from app_name.models import User
from app_name.forms import Login

@app.route('/')
def starter():
    return render_template('starter.html')