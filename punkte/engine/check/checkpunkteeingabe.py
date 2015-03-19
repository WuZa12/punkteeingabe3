__author__ = 'nicobrunnet'

def checkpunkteeingabe(id, matrikel, klausur, punktef1, punktef2, punktef3, punktef4, punktef5):
    if not checkint(id):
        return False
    if not checkint(matrikel):
        return False
    if not checkint(klausur):
        return False
    if not checkint(punktef1):
        return False
    if not checkint(punktef2):
        return False
    if not checkint(punktef3):
        return False
    if not checkint(punktef4):
        return False
    if not checkint(punktef5):
        return False
    return True

def checkint(zahl):
    check = True
    try: int(zahl)
    except ValueError:
        check2=False
    return checkint