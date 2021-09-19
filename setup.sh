
""" APP ENV """
export FLASK_APP=app
export ENV='development'
export FLASK_DEBUG=True

""" DATABSE ENV """
export DATABASE_URL='postgres://ohimydbamxhozq:4874b53b0e2a0403128a5f871f3007ea9e90c04c5f0c7590b24ae6b60ef1cfb1@ec2-63-32-7-190.eu-west-1.compute.amazonaws.com:5432/d59sliljil0g1o' # this only for developing
export DATABASE_TRACK_MODIFICATIONS = true

""" AUTH ENV """
export AUTH0_DOMAIN = "fax.us.auth0.com"
export ALGARITHMS = "RS256"
export API_AUDIENCE = "agency"

""" TOKENS MUST REUIREED! """
export PRODCUER_TOKEN = ""
export DIRECTOR_TOKEN = ""