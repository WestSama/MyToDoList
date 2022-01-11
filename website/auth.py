from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .dbmodel import User, Notes
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint("login", __name__)

# SignUp route 
@auth.route("/signup", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists.", category="error")
        elif len(username) < 4:
            flash("Username must have more than 4 characters.", category="error")
        elif len(password) < 7:
            flash("Password must have atleast 7 characters.", category="error")
        elif email != "@" and len(email) < 8:
            flash("Invalid email", category="error")
        else:
            # Add user to database
            newUser = User(username=username, email=email, password=generate_password_hash(password, method="sha256"))
            db.session.add(newUser)
            db.session.commit() 
            login_user(newUser, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("view.home"))

    return render_template("signup.html", user=current_user)

# Login route
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("You've logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("view.home"))
            else:
                flash("Incorrect password.", category="error")
        else:
            flash("Username does not exist.", category="error")
    return render_template("login.html", user=current_user)

# Logout route
@auth.route("/logout")
@login_required
def logout():
    session.pop("user", None)
    logout_user()
    return redirect(url_for("login.login"))

