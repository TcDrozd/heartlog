from flask import render_template, request, redirect, url_for, jsonify, session
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
        # Call the categorize API
        response = requests.post(
            'http://localhost:5050/api/categorize',
            json={'description': description},
            timeout=10
        )
        result = response.json()
        suggested_category = result.get('category', '')
        reasoning = result.get('reasoning', '')
        # If your API returns the whole JSON string, parse it


        # Store in session or pass via redirect (for MVP, session is easiest)
        session['entry_data'] = {
            'description': description,
            'category': suggested_category,
            'reasoning': reasoning
        }
        return redirect(url_for('confirm_entry'))
    return render_template('add_entry.html')

@app.route('/history')
def history():
    entries = Entry.query.filter_by(user_id=1).order_by(Entry.created_at.desc()).all()
    return render_template('history.html', entries=entries)

@app.route('/confirm', methods=['GET', 'POST'])
def confirm_entry():
    entry_data = session.get('entry_data')
    if not entry_data:
        return redirect(url_for('add_entry'))
    
    if request.method == 'POST':
        # User confirmed (possibly with a changed category)
        description = entry_data['description']
        category = request.form.get('category', entry_data['category'])
        reasoning = entry_data['reasoning']
        user_id = 1  # or your actual user system
        entry = Entry(
            user_id=user_id,
            description=description,
            love_language=category,
            auto_categorized=True,
            # Optionally, store reasoning if you add a column for it
        )
        db.session.add(entry)
        db.session.commit()
        session.pop('entry_data', None)
        return redirect(url_for('history'))

    return render_template('confirm_entry.html', entry=entry_data)