from database.models import Actors, Movies, drop_data_create_again


def insert_data():

	# actors
	actor1 = Actors(
	name='Sarah Cameron'
	,age='23'
	,gender='famale')
	actor1.insert()

	actor2 = Actors(
	name='Woody'
	,age='12'
	,gender='male')	
	actor2.insert()

	actor3 = Actors(
	name='Endy'
	,age='20'
	,gender='male')	
	actor3.insert()

	actor4 = Actors(
	name='Jhon'
	,age='57'
	,gender='famale')
	actor4.insert()

	actor5 = Actors(
	name='Tony'
	,age='48'
	,gender='male')
	actor5.insert()

	# movies
	movie1 = Movies(
	title = 'ToyStory 3',
	release_data = '13.11.1999')
	movie1.insert()

	movie2 = Movies(
	title = 'Avengers',
	release_data = '01.05.2015')
	movie2.insert()

	movie3 = Movies(
	title = 'Jhon Wick',
	release_data = '02.09.2017')
	movie3.insert()

	movie4 = Movies(
	title = 'Sarah Cameron',
	release_data = '20.09.2.021')		
	movie4.insert()
