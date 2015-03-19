__author__ = 'Nico'
from flask import request, render_template
from punkte import app
from punkte.db.verbindung import connect_db
from punkte.engine.alleNoten import getAlleNoten
import sqlite3


@app.route('/alleNoten', methods=['GET', 'POST'])
def alleNoten():
    con = sqlite3.connect(connect_db())
    cu = con.cursor()

    #cu.execute("""CREATE TABLE noten (id INTEGER, matrikel INTEGER,
     #             klausur INTEGER, Frage1 INTEGER, Frage2 INTEGER,
      #            Frage3 INTEGER, Frage4 INTEGER, Frage5 INTEGER)""")
    #con.commit()

    cu.execute('SELECT * FROM noten')

    noten = [dict(id=r[0], matrikel=r[1], klausur=r[2], f1=r[3], f2=r[4],
                  f3=r[5], f4=r[6], f5=r[7], ) for r in cu.fetchall()]
    cu.close()
    con.close()

    noten = getAlleNoten()

    return render_template('alleNoten.html', noten=noten)