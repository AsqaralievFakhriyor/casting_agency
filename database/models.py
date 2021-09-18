import os
from sqlalchemy import Column, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

#geting database url


db = SQLAlchemy()

# setup function 
def setup_db(app):
	app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://ohimydbamxhozq:4874b53b0e2a0403128a5f871f3007ea9e90c04c5f0c7590b24ae6b60ef1cfb1@ec2-63-32-7-190.eu-west-1.compute.amazonaws.com:5432/d59sliljil0g1o'
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	db.app = app
	# grabing configurations from config.py
	# app.config.from_object('config')
	db.init_app(app)
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
