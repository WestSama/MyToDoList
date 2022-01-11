from flask import Blueprint, render_template, request, flash, redirect, session
from flask_sqlalchemy import sqlalchemy
from flask.helpers import flash, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from .dbmodel import Notes, Archive
from . import db

view = Blueprint("view", __name__)

# Homepage Route
@view.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
    
        note = request.form.get("todo")
        select = request.form.get("select")
        
        userID = current_user.id
        
        if len(note) < 5:
            flash("ToDo is too short!", category="error")
        else:
            if select == "1":
                db.engine.execute("INSERT INTO notes(text, time, status, user_id) VALUES(?, CURRENT_TIMESTAMP, 'True', ?)", note, userID)
            else:
                db.engine.execute("INSERT INTO notes(text, time, status, user_id) VALUES(?, CURRENT_TIMESTAMP, 'False', ?)", note, userID)
            #flash("ToDo has been added.", category="success")
            return redirect("/")
        print(select)
    return render_template("index.html", user=current_user)

# Show user Archive
@view.route("/archive", methods=["POST","GET"])
@login_required
def archive():
    if request.method == "GET":
        test = db.engine.execute("SELECT * FROM archive ORDER BY id ASC")
        return render_template("archive.html", user=current_user, test=test)

# Delete in the archive
@view.route("/<int:id>/archive", methods=["POST"])
def archiveDelete(id):   
    todoDelete = Archive.query.get(id)

    if request.method == "POST":
        db.session.delete(todoDelete)
        db.session.commit()
        return redirect(url_for("view.archive"))
    else:
        return "There was a problem deleting..."
    
# Delete ToDo route
@view.route("/<int:id>/delete/", methods=["POST"])
def delete(id):
    todoDelete = Notes.query.get(id)
    todoDelete2 = Archive.query.get(id)

    if request.method == "POST":
        if todoDelete:
            db.session.delete(todoDelete)
        elif todoDelete2:
            db.session.delete(todoDelete2)
        db.session.commit()
        return redirect(url_for("view.home"))
    else:
        return "There was a problem deleting..."

# Delete from index and add to Archive
@view.route("/<int:id>/delete2/", methods=["POST"])
def delete2(id):
    todoDelete = Notes.query.get(id)

    if request.method == "POST":
        db.engine.execute("INSERT INTO archive(text, time, user_id) SELECT text, time, user_id FROM notes WHERE id=?", id)
        db.session.delete(todoDelete)
        db.session.commit()
        return redirect(url_for("view.home"))
    else:
        return "There was a problem deleting..."

# Delete All ToDo route
@view.route("/delete/", methods=["POST"])
def deleteAll():

    if request.method == "POST":
        db.session.query(Notes).delete()
        db.session.commit()
        return redirect(url_for("view.home"))
    else:
        return "There was a problem deleting..."

# Delete All in Archive
@view.route("/delarchive/", methods=["POST"])
def archiveDeleteAll():

    if request.method == "POST":
        db.session.query(Archive).delete()
        db.session.commit()
        return redirect(url_for("view.archive"))
    else:
        return "There was a problem deleting..."
