import os
from sqlalchemy import Column, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


#geting database url
# DB_PATH = os.getenv('DATABASE_URL')


db = SQLAlchemy()

# setup function 
def setup_db(app):
	# app.config["SQLALCHEMY_DATABASE_URI"] = database_path
	# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = flask_sqlalchemy 
	db.app = app
	# grabing configurations from config.py
	app.config.from_object('config')
	db.init_app(app)
	db.create_all()

def drop_data_create_again():
	db.drop_all()
	db.create_all()
# actors 
class Actors(db.Model):

	__tablename__ = 'actors'

	id = Column(Integer, primary_key = True)
	name = Column(String(50))
	age = Column(Integer)
	gender = Column(String(120))

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def insert(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def format(self):
		return {
				'id': self.id,
				'name': self.name,
				'age': self.age,
				'gender': self.gender
			}

# movies

class Movies(db.Model):

	__tablename__ = 'movies'
	id = Column(Integer, primary_key= True)
	title = Column(String(120))
	release_data = Column(String(120))

	def __init__( self, title, release_data):
		self.title = title 
		self.release_data = release_data

	def insert(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def format(self):
		return {
			'id': self.id,
			'title': self.title,
			'release_data': self.release_data
		}
