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

	def student_remove(self,student_id):
		"""Deletes a student
		"""
		query1=self.session.query(Student).filter(Student.id==student_id).one()
		
		if student_id:
			self.session.delete(query1)
			self.session.commit()
			click.secho(("Deleted student " + "'%s'" + " succesfully.") % (student_id), fg='green')
		else:
			click.secho("Warning! student[id] cannot be empty.", fg='red')

	def class_add(self,name):
		"""Adds a class
		"""

		if name:
			new_class = Class(name=name)
			self.session.add(new_class)
			self.session.commit()
			click.secho(("Added class '{}' succesfully.").format(name), fg='green')
		else:
			click.secho("Warning! class [name] cannot be empty.", fg='red')

	def class_remove(self,class_id):
		"""Deletes a class
		"""
		query1=self.session.query(Class).filter(Class.id==class_id).one()
		
		if class_id:
			self.session.delete(query1)
			self.session.commit()
			click.secho(("Deleted class with id '{}' succesfully.").format(class_id), fg='green')
		else:
			click.secho("Warning! class[id] cannot be empty.", fg='red')
		
if __name__ == '__main__':
	Database().cmdloop()
