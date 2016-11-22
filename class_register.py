from termcolor import cprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click


from models.models import Base,Student,Class,TrackStudent

engine =  create_engine('sqlite:///classregister.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

class Database(object):
	session = DBSession()

	def __init__(self):
		pass

	def student_add(self,name):
		"""Adds a student
		"""

		if name:
			new_student = Student(name=name)
			self.session.add(new_student)
			self.session.commit()
			click.secho(("Added student " + "'%s'" + " succesfully.") % (name), fg='green')
		else:
			click.secho("Warning! students'[name] cannot be empty.", fg='red')

if __name__ == '__main__':
	Database().cmdloop()
