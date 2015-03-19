__author__ = 'Nico'
from flask import Flask

app = Flask(__name__)

import punkte.routes
import punkte.static
import punkte.templates
import punkte.db
import punkte
import punkte.engine.check
import punkte.engine