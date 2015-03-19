__author__ = 'Nico'
from flask import render_template
from punkte import app

# ruft die index-seite auf:
@app.route('/')
def home():
    return render_template('anzeigeHome.html')