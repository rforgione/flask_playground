from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='assets/templates/')
app.config.from_object('config')
db = SQLAlchemy(app)

from app.api import *
from app.views import *
from app.routing import *
from app.dbtools import *
from app.models import *
