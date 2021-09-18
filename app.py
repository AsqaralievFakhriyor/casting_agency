import os
from flask import (
	Flask,  
	jsonify, 
	abort, 
	redirect, 
	url_for,
	render_template)
from flask import request
import json
from flask_cors import CORS
from database.models import setup_db, Actors, Movies, drop_data_create_again
from auth.auth import AuthError, requires_auth
from helpers import insert_data

# from authlib.integrations.flask_client import OAuth

def create_app(test_config=None):

	app = Flask(__name__)

	# I tried to get token and via json to user, more info in log result route

	# oauth = OAuth(app)

	# auth0 = oauth.register(
	# 'auth0',
	# client_id='l4ZqjZ7B3vtqJkrA3fU5wbw3cKXgyJ8k',
	# client_secret='6-uHXRbBjvFh1717iT0lX0MU0RXptwinW0I12g0pM82hn2L8OSc_-FS5BBLgcgwe',
	# api_base_url='https://fax.us.auth0.com',
	# access_token_url='https://fax.us.auth0.com/oauth/token',
	# authorize_url='https://fax.us.auth0.com/authorize',
	# client_kwargs={
	# 	'scope': 'openid profile email',
	# 	},
	# )

	setup_db(app)
	CORS(app)
	drop_data_create_again()
	insert_data()

	@app.after_request
	def after_request(response):

		response.headers.add('Access-Conrool-Allow-Headers', 'Content-Type, Authorization, true')
		response.headers.add('Access-Conrool-Allow-Methods', 'GET, POST, PUT, PATCH, OPTION')

		return response

	# database data filter helper 

	def actor_helper():
		actors = Actors.query.all()
		all_actors = [actor.format() for actor in actors]
		return all_actors

	def movie_helper():
		movies = Movies.query.all()
		all_movies = [movie.format() for movie in movies]
		return all_movies

	#---------------------------------------------------------#	
	# endpoints 
	#---------------------------------------------------------#
	@app.route('/')
	def index():
		return jsonify({
			"Ok page is working!"
			})

	# GET endpoint for actors
	@app.route('/actors', methods = ['GET'])
	def actors():
		# @requires_auth('get:actors') ---> i reved this, couse i needed to create another email to make another role, but i didnt have eneugh time, i am sorry! 
		try:
			actors = actor_helper()
		except:
			abort(404)
		finally:
			return jsonify({
				'success': True,
				'actors': actors,
				})

	# GET endpoint for movies
	@app.route('/movies', methods = ['GET'])
	def movies():# @requires_auth('get:movies') ---> i removed this becouse i needed another email to make another role, 

		try:
			movies = movie_helper()
		except:
			abort(404)
		finally:
			return jsonify({
				'success': True,
				'movies': movies
				})

	#---------------------------------------------------------#
	# POST endpoint for actors
	@app.route('/actors', methods = ['POST'])
	@requires_auth('post:actors')
	def post_actors(jwt):

		body = request.get_json()
		name = body.get('name', None)
		age = body.get('age', None)
		gender =  body.get('gender', None)


		if (name is None) or (age is None) or (gender is None):
			abort(400)

		try:
			new_actor = Actors(
			name = name,
			age = age,
			gender = gender)

			new_actor.insert()
			actor = [new_actor.format()]

			return jsonify({
				'success': True,
				'status_code': 200,
				'actor': actor
				})
		except:
			abort(422)

	# POST endpoint for movies
	@app.route('/movies', methods = ['POST'])
	@requires_auth('post:movies')
	def post_movies(jwt):

		body = request.get_json()
		title = body.get('title', None)
		release_data = body.get('release_data', None)

		if (title is None) or (release_data is None):
			abort(400)

		try:
			new_movie = Movies(
			title = title,
			release_data = release_data)

			new_movie.insert()
			movie = [new_movie.format()]

			return jsonify({
				'success': True,
				'status_code': 200,
				'movie': movie
				})
		except:
			abort(422)

	#---------------------------------------------------------#
	# PATCH endpoint for actors
	@app.route('/actors/<int:actor_id>', methods = ['PATCH'])
	@requires_auth('patch:actors')
	def patch_actors(jwt, actor_id):

		if not actor_id: 
			abort(404)

		body = request.get_json()
		name = body.get('name', None)
		age = body.get('age', None)
		gender = body.get('gender', None)

		if (name is None) and (age is None) and (gender is None):
			abort(400)

		actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
			
		if actor is None:
			abort(404) 

		try:
			if name:
				actor.name = name
			if age:
				actor.age = age
			if gender:
				actor.gender = gender

			actor.update()
			actor = [actor.format()]

			return jsonify({
				'success': True,
				'status_code': 200,
				'actor': actor
				})
		except:
			abort(422)

	# PATCH endpoint for movies
	@app.route('/movies/<int:movie_id>', methods = ['PATCH'])
	@requires_auth('patch:movies')
	def patch_movies(jwt, movie_id):

		if not movie_id: 
			abort(404)

		body = request.get_json()
		title = body.get('title', None)
		release_data = body.get('release_data', None)

		if (title is None) and (release_data is None):
			abort(400)

		movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
		if movie is None:
			abort(404)

		try:
			movie.title = title
			movie.release_data = release_data

			movie.update()
			movie = [movie.format()]

			return jsonify({
				'success': True,
				'status_code': 200,
				'movie': movie
				})
		except:
			abort(422)

	#---------------------------------------------------------#
	# DELETE endpoint for actors
	@app.route('/actors/<int:actor_id>', methods = ['DELETE'])
	@requires_auth('delete:actors')
	def delte_actors(jwt, actor_id):

		if not actor_id:
			abort(404)

		actor = Actors.query.filter(Actors.id==actor_id).one_or_none()

		if actor is None:
			abort(404)

		try:
			actor = Actors.query.filter(Actors.id==actor_id).one_or_none()

			if actor is None:
				abort(404)

			actor.delete()

			return jsonify({
				'success': True,
				'status_code': 200,
				'deleted': actor_id,
				'message':'deleted successfully'
				})
		except:
			abort(422)

	# DELETE endpoint for movies

	@app.route('/movies/<int:movie_id>', methods = ['DELETE'])
	@requires_auth('delete:movies')
	def delte_movies(jwt, movie_id):

		if not movie_id:
			abort(404)

		movie = Movies.query.filter(Movies.id==movie_id).one_or_none()

		if movie is None:
			abort(404)

		try:
			movie.delete()

			return jsonify({
				'success': True,
				'status_code': 200,
				'deleted': movie_id,
				'message':'deleted successfully'
				})
		except:
			abort(422)

	# log results i tried it but i think it tooks a bit time so i will do it after getting sertifacate if i can :)
	# @app.route('/log-result', methods=['GET', 'POST'])
	# def log_result():
	# 	if True:
	# 		response = auth0.authorized_response()
	# 		print(response.get("id_token"))
	# 		return jsonify({
	# 			'your authorization token': token,
	# 			'success': True,
	# 			'message': 'That token is only for developing purposes,'
	# 			})
	# 	else:
	# 		raise AuthError({
 #            	'code':'authorization_header_missing',
 #            	'description': 'Authorization header expected'
 #            	}, 401)
	#---------------------------------------------------------#
	# ERROR hanlders

	@app.errorhandler(422)
	def unprocessable(error):
	    return jsonify({
	        "success": False,
	        "error": 422,
	        "message": "unprocessable"
	    }), 422

	@app.errorhandler(400)
	def bad_request(error):
	    return jsonify({
	        "success": False,
	        "error": 400,
	        "message": "bad request"
	    }), 400

	@app.errorhandler(404)
	def not_found(error):
	    return jsonify({
	        "success": False,
	        "error": 404,
	        "message": "not found"
	    }), 404

	# auth errorhandlers
	@app.errorhandler(AuthError)
	def auth_error_handler(AuthError):
		return jsonify({
	        		"error": AuthError.status_code,
	        		"message": AuthError.error["description"],
	        		"success": False,
	    			}), AuthError.status_code




	return app