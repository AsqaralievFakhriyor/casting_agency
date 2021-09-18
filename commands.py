import click
from falsk.cli import with_appcontext

from database models import db, Actors, Movies

@click.command(name='create_tables')
@with_appcontext
def create_tables():
	db.create_all()
# actually this didnt worked on heroku but i will try it soon :)