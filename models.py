from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

LOVE_LANGUAGES = [
    ("acts_of_service", "Acts of Service"),
    ("quality_time", "Quality Time"),
    ("receiving_gifts", "Receiving Gifts"),
    ("words_of_affirmation", "Words of Affirmation"),
    ("physical_touch", "Physical Touch"),
    ("other", "Other"),
]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.now)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    love_language = db.Column(db.String(32))
    auto_categorized = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship('User', backref=db.backref('entries', lazy=True))

class Couple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)