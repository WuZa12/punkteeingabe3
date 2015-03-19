__author__ = 'Nico'
from flask import request, render_template
from punkte import app
from punkte.db.verbindung import connect_db
import sqlite3


def getAlleNoten():
    con = sqlite3.connect(connect_db())
    cu = con.cursor()


    cu.execute('SELECT * FROM noten')

    noten = [dict(id=r[0], matrikel=r[1], klausur=r[2], f1=r[3], f2=r[4],
                  f3=r[5], f4=r[6], f5=r[7], ) for r in cu.fetchall()]
    cu.close()
    con.close()

    return noten