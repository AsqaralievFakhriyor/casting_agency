import os
from app import create_app
from database.models import setup_db, Movies, Actors
import unittest
import json
from config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy

# i imported this function becouse git freezed when i runned this file   
test_actor = Actors(
    name='Mark',
    age='32',
    gender='male')

test_movie = Movies(
    title='Alone in Mars',
    release_data='14.07.2045')

class CapstoneTest(unittest.TestCase):
    def setUp(self):

        # DB_PATH = os.getenv('DATABASE_URL_TEST')
        self.app = create_app()
        self.client = self.app.test_client
        self.praducer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpYdEhxdFY2S3B3UzhVMGFHRFRocCJ9.eyJpc3MiOiJodHRwczovL2ZheC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0NGEzZGQ3NTczNjQwMDZhMDllYzY1IiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNjMxOTg3ODY0LCJleHAiOjE2MzE5OTUwNjQsImF6cCI6Imw0WnFqWjdCM3Z0cUprckEzZlU1d2J3M2NLWGd5SjhrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.QXhD37ONB6IeFGqiPGo4Y2afD-2f6og6CY8bDk6o3TiLoXCz5-rFowAlRFydhM_tDPGpEXuO3yhbR2CMxfIDWyaVZuvrHSmHSVurXyw56hJcU0XReuP2b59KAIVRIcH_IypWj6C_vtqkZ0v34ZR19QW-4It9B4le52kBSSaHGToJiPlgwHHQJFgTTo4xupz0ervHoQgolpvnJ-m3L0prt6dHCbefFPk3MhNfCi_y_AAnHMCutdhAmhrlplrI42S-_YZjkAxrw66HQr2kBF4B5a3pV12YcnVYeANtM-9rZuazzRvuYtJF4kGqE5kumRDS0wdp877mTw5sQ12KHaIHiQ'
        self.director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpYdEhxdFY2S3B3UzhVMGFHRFRocCJ9.eyJpc3MiOiJodHRwczovL2ZheC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0NDgzZTYwMDU3NGYwMDcwMTI4MmMxIiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNjMxOTg3Nzg0LCJleHAiOjE2MzE5OTQ5ODQsImF6cCI6Imw0WnFqWjdCM3Z0cUprckEzZlU1d2J3M2NLWGd5SjhrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.EE-YntLNAIieOuqLvsiqGRjB31_8ILNnrl1YBlLX0nzaj5xFbUjy4BRauv7Zd_uDWSvbDODZZUkLvoCtITc-mih6SgZJCI8HJ4M0zh4cZk04nN2w9n4wCkXx2hS3bfwMapwV2Bv48P_JsftfM2vBz2BVGUFY_-cuofixHvE-C-al2VUeOdAgPKB8q40_bXWR9MQiugGKfyLkysAFSSP1uf2yki4igwNTBwrqPd5JNZ-ipmD6p5fnGR9iDHq6_8KYzUNP-sBZ2m10m2AvWWQBQdMEQ0MuqlotQCmjDLIEDDxy-AD_ZkRz8-D9k1rXksLQWTQDDxYRhtAO9GeS1pbz7w'
        self.test_actor_data = {"name": "Emerson", "age": 20, "gender":"male"}
        self.test_movie_data = {"title": "Avatar", "release_data":"20.09.2021"}

        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables 
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass


    # test for actors endpoints 
    def test_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_post_actor(self):
        response = self.client().post('/actors',
            json=self.test_actor_data,
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor'][0]['name'], 'Emerson')
        self.assertEqual(data['actor'][0]['age'], 20)
        self.assertEqual(data['actor'][0]['gender'], 'male')

    def test_post_actor_400(self):
        response = self.client().post('/actors',
            json={},
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_post_actor_unauthorized_401(self):
        response = self.client().post('/actors',
            json=self.test_actor_data)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], 'Authorization header expected')

    def test_patch_actor(self):
        new_actor = {"name": "Lily", "age": 19, "gender": "female"}
        response = self.client().patch('/actors/1',
            json=new_actor,
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        data_actor = data['actor'][0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data_actor['name'], 'Lily')
        self.assertEqual(data_actor['age'], 19)
        self.assertEqual(data_actor['gender'], 'female')

    def test_patch_actor_400(self):
        response = self.client().patch('/actors/1',
            json={},
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_patch_actor_unauthorized_401(self):

        new_actor = {"name": "Lily", "age": 19, "gender": "female"}
        response = self.client().patch('/actors/1',json=new_actor)

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], 'Authorization header expected')

    def test_patch_actor_404(self):
        new_actor = {"name": "Lily", "age": 19, "gender": "female"}
        response = self.client().patch('/actor/1000',
            json=new_actor,
            headers={'Authorization': f'Bearer {self.praducer_token}'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'not found')


    def test_delete_actor(self):
        test_actor.insert()
        response = self.client().delete(f'/actors/{test_actor.id}',
            headers={'Authorization': f'Bearer {self.director_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertEqual(data['deleted'], test_actor.id)

    def test_delete_actor_401(self):
        response = self.client().delete('/actors/3')

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 401)
        self.assertEqual(data['message'], 'Authorization header expected')

    def test_delete_actor_404(self):
        response = self.client().delete('/actors/1000',
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    # tests for movies endpoinds ############################################
    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_post_movie(self):
        response = self.client().post('/movies',
            json=self.test_movie_data,
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertEqual(data['movie'][0]['title'], 'Avatar')
        self.assertEqual(data['movie'][0]['release_data'],'20.09.2021')

    def test_post_movie_400(self):
        response = self.client().post('/movies', 
            json={}, 
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    
    def test_post_movie_unauthorized_401(self):
        response = self.client().post('/movies',
            json=self.test_movie_data,
            headers={'Authorization': f'Bearer {self.director_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['error'], 403)
        self.assertEqual(data['message'], 'To complate command permission needed')

    def test_patch_movie(self):
        response = self.client().patch('/movies/1',
            json=self.test_movie_data,
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        data_movie = data['movie']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data_movie[0]['title'], 'Avatar')
        self.assertEqual(data_movie[0]['release_data'],'20.09.2021')

    def test_patch_movie_400(self):
        response = self.client().patch('/movies/2',
            json={},
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')

    def test_delete_movie(self):

        test_movie.insert()
        response = self.client().delete(f'/movies/{test_movie.id}',
            headers={'Authorization': f'Bearer {self.praducer_token}'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertEqual(data['deleted'], test_movie.id)

    def test_delete_movie_401(self):

        response = self.client().delete(f'/movies/4',
            headers={'Authorization': f'Bearer {self.director_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['error'], 403)
        self.assertEqual(data['message'], 'To complate command permission needed')

    def test_delete_movie_404(self):
        response = self.client().delete('/movies/10000',
            headers={'Authorization': f'Bearer {self.praducer_token}'})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

if __name__ == "__main__":
    unittest.main()