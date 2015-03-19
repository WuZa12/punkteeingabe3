__author__ = 'Nico'
from flask import request, render_template
from punkte import app
from punkte.db.verbindung import connect_db
from punkte.engine.alleNoten import getAlleNoten
from punkte.engine.punkteeingabedb import punkteeingabedb
import sqlite3


@app.route('/eingabe', methods=['GET', 'POST'])
def punkteeingabe():
    con = sqlite3.connect(connect_db())
    cu = con.cursor()
    id = request.form['id']
    klausur = request.form['klausur']
    matrikel  = request.form['matrikel']
    punktef1 = request.form['punktef1']
    punktef2 = request.form['punktef2']
    punktef3 = request.form['punktef3']
    punktef4 = request.form['punktef4']
    punktef5 = request.form['punktef5']

    if not (punkteeingabedb(id, matrikel, klausur, punktef1, punktef2, punktef3, punktef4, punktef5)):
        error = "bitte die eingabe ueberpruefen"
        return render_template('punkteeingabe.html', error=error)


    noten = getAlleNoten()
    cu.close()
    con.close()

    return render_template('alleNoten.html', noten=noten)