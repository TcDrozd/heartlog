from flask import render_template, request, redirect, url_for, jsonify
import requests
from app import app
from models import db, Entry, User


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        description = request.form['description']
        love_language = request.form['love_language']
        # For now, assume user_id=1
        entry = Entry(user_id=1, description=description, love_language=love_language)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('history'))
    return render_template('add_entry.html')

@app.route('/history')
def history():
    entries = Entry.query.filter_by(user_id=1).order_by(Entry.created_at.desc()).all()
    return render_template('history.html', entries=entries)

