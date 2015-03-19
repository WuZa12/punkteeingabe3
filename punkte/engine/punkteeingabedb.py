__author__ = 'nicobrunnet'
from flask import request, render_template
from punkte import app
from punkte.db.verbindung import connect_db
from punkte.engine.check.checkpunkteeingabe import checkpunkteeingabe
from punkte.engine.check.checkNULL import checknull
import sqlite3


def punkteeingabedb(id, matrikel, klausur, punktef1, punktef2, punktef3, punktef4, punktef5):
    con = sqlite3.connect(connect_db())
    cu = con.cursor()

    if not (checknull(id) & checknull(matrikel) & checknull(punktef1) & checknull(punktef2) &
            checknull(punktef3) & checknull(punktef4) & checknull(punktef5)):
        return False

    if not checkpunkteeingabe(id, matrikel, klausur, punktef1, punktef2, punktef3, punktef4, punktef5):
        return False



    cu.execute('INSERT into noten (id, matrikel, klausur, '
           'Frage1, Frage2, Frage3, Frage4, Frage5) '
           'values (%s, %s, %s, %s, %s, %s, %s, %s)' %
           (id, matrikel, klausur, punktef1, punktef2, punktef3, punktef4, punktef5))

    con.commit()
    cu.close()
    con.close()