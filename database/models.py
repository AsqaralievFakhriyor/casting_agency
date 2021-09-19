import os
from sqlalchemy import Column, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json



db = SQLAlchemy()

# setup function 
def setup_db(app):
	DATABASE_URL = os.getenv("DATABASE_URL")
	DATABASE_TRACK_MODIFICATIONS = os.getenv("DATABASE_TRACK_MODIFICATIONS")
	app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = DATABASE_TRACK_MODIFICATIONS
	db.app = app
	db.init_app(app)
	db.session.commit()
	db.drop_all()
	db.create_all()

""" Super Class for helper commands"""

class superClass(db.Model):
    __abstract__ = True

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# actors 
class Actors(superClass):
	__tablename__ = 'actors'

	id = Column(Integer, primary_key = True)
	name = Column(String(50))
	age = Column(Integer)
	gender = Column(String(120))

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender


	def format(self):
		return {
				'id': self.id,
				'name': self.name,
				'age': self.age,
				'gender': self.gender
			}

# movies
class Movies(superClass):

	__tablename__ = 'movies'

	id = Column(Integer, primary_key= True)
	title = Column(String(120))
	release_data = Column(String(120))

	def __init__( self, title, release_data):
		self.title = title 
		self.release_data = release_data

	def format(self):
		return {
			'id': self.id,
			'title': self.title,
			'release_data': self.release_data
		}
