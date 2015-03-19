__author__ = 'Nico'
from flask import request, render_template
from punkte import app
from punkte.db.verbindung import connect_db
import sqlite3


@app.route('/maskeeingabe', methods=['GET', 'POST'])
def maskeeingabe():
    con = sqlite3.connect(connect_db())
    cu = con.cursor()

    cu.close()
    con.close()
    return render_template('punkteeingabe.html')