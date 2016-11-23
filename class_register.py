from termcolor import cprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
import calendar
from datetime import datetime
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

	def log_start(self,class_id):
		"""Creates a new time log for a particular class.
		"""
		if class_id:			
			now = datetime.now()
			query1=self.session.query(Class).filter(Class.id==class_id)
			query2=query1.one()
			query2.class_start_time=now
			query2.class_in_session=True
			self.session.commit()
			click.secho("Class {} has started".format(class_id), fg='green')
		else:
			click.secho("Warning! class[id] cannot be empty.", fg='red')

	def log_end(self,class_id):
		"""Ends a time log for a class that
		has already been started.
		"""
		if class_id:			
			now = datetime.now()
			query1=self.session.query(Class).filter(Class.id==class_id)
			query2=query1.one()
			if query2.class_in_session==1:
				query2.class_in_session=False
				query2.class_end_time=now
				self.session.commit()
				click.secho("Class {} has ended".format(class_id), fg='green')
			elif query2.class_in_session==0:
				click.secho("Warning! Class {} has not started.".format(class_id), fg='red')
			else:
				click.secho("Warning! class[id] cannot be empty.", fg='red')

if __name__ == '__main__':
	Database().cmdloop()
