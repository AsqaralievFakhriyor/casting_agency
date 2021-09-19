# Casting Agency Udacity Full-stack final project 🙂
### This project was maded only for learning purposes!😉

# Casting Agency Specifications
[!]**NOTE:** The Project was Deployed on Heroku and Working I think 😅
> https://casting_agencym.herokuapp.com 

## The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Models:
1. Movies with attributes title and release data.
2. Actors with attributes name, age and gender
#### I dont have relationship databases, i can make them but i dont have time, i must do my 4th project untill 20.09.2021 please dont ask me to do them 😥

## Endpoinds:🍔
1. GET /actors and /movies
2. DELETE /actors/ and /movies/
3. POST /actors and /movies and
4. PATCH /actors/ and /movies/

## Roles:
### Casting Assistant 😊
1. Can view actors and movies
### Casting Director 😎
1. All permissions a Casting Assistant has and…
2. Add or delete an actor from the database
3. Modify actors or movies
### Executive Producer 🧐
1. All permissions a Casting Director has and…
2. Add or delete a movie from the database

## Tests:
1. One test for success behavior of each endpoint
2. One test for error behavior of each endpoint
3. At least two tests of RBAC for each role

## In Casting Agency i have to users with roles
1. asqaraliyev01@gmail.com -> Casting Director
2. asqaraliyev07@gamil.com -> Executive Producer
## Password for all users: 12345678Qwe

# Authorization Link: 
>[!] Copy the `link` bellow end open with your borwser

```language

https://fax.us.auth0.com/authorize?audience=agency&response_type=token&client_id=l4ZqjZ7B3vtqJkrA3fU5wbw3cKXgyJ8k&redirect_uri=http://127.0.0.1:5000/log-result

```

![auth_login](/screenshots/auth_login.jpg)

### You can copy access token from Link after authorizatino

![token_screen](/screenshots/token_screen.jpg)

### After geting acces token you have to save to [`setup.sh`](/setup.sh) or to heroku's evniroments
### And if you want you can change DATABASE_URL, AUTH0_AUDIANCE, AUTH0_DOMAIN etc, environments too 

## Installing Dependencies
>[!] Python-3.9.5 (recommended)

### Virtual Environment

```bash

cd project_directory
pip install venv
python -m venv venv
source venv/Script/active

```

### PIP Dependecies
> Once you have your **venv** setup and running, install dependencies by navigating
> to the root directory and running:
```bash
pip install -r requirements.txt
```
>This will install all of the required packages included in the requirements.txt
>file.

### Exporting ENV VARIABES form setup.sh file
```bash
source setup.sh
```

### Local Database Setup
> Once you create the database, open your terminal, navigate to the root folder, and run:
```bash
flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
```
>[!] After running, don't forget modify 'SQLALCHEMY_DATABASE_URI' variable.

### TO `upgrade` DATABASE on `HEROKU` use:
```bash
	python manage.py db init
	python manage.py db migrate
	python manage.py db upgrade
```
## Local Testing
> To test your local installation, run the following command from the root folder:
```bash
python -m test_ap.py
```
> If all tests pass, your local installation is set up correctly.

## Runing the Server
> From within the root directory, first ensure you're working with your created
venv. To run the server, execute the following:
```bash

flask run

```
> Setting the FLASK_ENV variable to development will detect file changes and
> restart the server automatically.
> Setting the FLASK_APP variable to agency directs Flask to use
> the agency directory and the __init__.py file to find and load the
> application.

### Project is ready to deploy HEROKU but you need to add POSGRESQL addon to your [`HEROKU`](https://heroku.com)  aplications

##### 1. `GET` ACTORS

* Methods: **GET**
* URL: `/api/actors`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://casting-agencym.herokuapp.com/actors' \
--header 'Authorization: Bearer <token>'
```

Sample Request using Python:

```python
import requests

url = "https://casting-agencym.herokuapp.com/actors"

payload={}
headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

### `GET` - Movie endpoints

##### 1. `GET` MOVIES

* Methods: **GET**
* URL: `/movies`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://casting-agencym.herokuapp.com/movies' \
--header 'Authorization: Bearer <token>'
```

using Python:

```python
import requests

url = "https://casting-agencym.herokuapp.com/movies"

payload={}
headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

### `POST` - Actor endpoints

* Methods: **POST**
* URL: `/actors`
* Permission: `add:actors`

>[!] Required Request Body

Request body structure:

```json
{
    "name": str,
    "age": int,
    "gender": "male" or "famale"
}
```

Sample Request using Curl:

```bash
curl --location --request POST \
'https://casting-agencym.herokuapp.com/actors' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "Arnold Shvarsnegr",
	"age": 64,
	"gender": "male"
}'
```

Sample Request using Python:

```python
import requests

url = "https://casting-agencym.herokuapp.com/actors"

payload="{\r\n\t\"name\": \"Roan Atkinson\",\r\n\t\"age\": 57,\r\n\t\"gender\": \"male\"\r\n}"
headers = {
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

### `POST` - Movie endpoints

* Methods: **POST**
* URL: `/movies`
* Permission: `add:movies`

>[!] Required Request Body

Request body structure:

```json
{
    "title": str,
    "release_date": int,
}
```

Sample Request using Curl:

```bash
curl --location --request POST \
'https://casting-agencym.herokuapp.com/movies' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "Mr Bin",
	"release_date": "1985"
}'
```

Sample Request using Python:

```python
import requests

url = "https://casting-agencym.herokuapp.com/movies"

payload="{\r\n\t\"title\": \"Alisa and wonder world\",\r\n\t\"release_date\": \"1990\"\r\n}"
headers = {
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


```

### `PATCH` - Actor endpoints

* Methods: **PATCH**
* URL: `/actor/<id>`
* Permission: `update:actors`

>[!] Required Request Body

Request body structure:

```json
{
    "name": str,
    "age": int,
    "gender": "famale" or "male"
}
```

Sample Request using Curl:

```bash
curl --location --request PATCH \
'https://casting-agencym.herokuapp.com/actors/<id>' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "Jozeffa",
	"age":45,
	"gender":"famale"
}'
```

Sample Request using Python:

```python
import requests

url = "https://casting-agencym.herokuapp.com/actors/<id>"

payload="{\r\n\t\"name\": \"Sarah Conor\",\r\n\t\"age\":24,\r\n\t\"gender\":\"famale\"\r\n}"
headers = {
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
```

### `PATCH` - Movie endpoints

* Methods: **PATCH**
* URL: `/movie/<id>`
* Permission: `update:movies`

>[!] Required Request Body

Request body structure:

```json
{
    "title": str,
    "release_date": int,
}
```

Sample Request using Curl:

```bash
curl --location --request PATCH \
'https://casting-agencym.herokuapp.com/movies/<id>' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "King Kong",
	"release_date": "1988"
}'
```

Sample Request using Python:

```python
import requests

url = "https://casting-agencym.herokuapp.com/movies/<id>"

payload="{\r\n\t\"title\": \"King Kong\",\r\n\t\"release_date\": \"1988\"\r\n}"
headers = {
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
```

### `DELETE` - Actor endpoints

* Methods: **DELETE**
* URL: `/actor/<id>`
* Permission: `delete:actors`

>[!] Request body is not required

Sample request using CURL:

```bash
curl --location --request DELETE \
'https://casting-agencym.herokuapp.com/actors/1' \
--header 'Authorization: Bearer <token>'
```

Request using Python:

```python
import requests

url = "https://casting-agencym.herokuapp.com/actors/1"

payload={}
headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

### `DELETE` - Movie endpoints

* Methods: **DELETE**
* URL: `/movie/<id>`
* Permission: `delete:movies`

>[!] Request body is not required

Sample request using CURL:

```bash
curl --location --request DELETE \
'https://casting-agencym.herokuapp.com/movies/1' \
--header 'Authorization: Bearer <token>'
```

Request using Python:

```python
import requests

url = "https://casting-agencym.herokuapp.com/movies/1"

payload={}
headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

