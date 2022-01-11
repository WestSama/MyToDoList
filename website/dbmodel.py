from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Creating our tables for database

    
class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(15000))
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    status = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Archive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(15000))
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(80))
    notes = db.relationship("Notes")
    arch = db.relationship("Archive")

