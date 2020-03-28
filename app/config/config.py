import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


game = Flask(__name__, template_folder='../view', static_folder='../static')
game.config['SECRET_KEY'] = os.urandom(24)
game.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
game.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../record.db'

db = SQLAlchemy(game)