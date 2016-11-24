from termcolor import cprint
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import sessionmaker
import click
import calendar
from datetime import datetime
from prettytable import PrettyTable
from tabulate import tabulate
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

	def check_in(self,student_id,class_id):
		"""Checks in a student into a class at the current time.
		"""
		# Check current time
		now = datetime.now()
		# return class id in Class table
		get_class_id=self.session.query(Class).filter(Class.id==class_id).one()
		
		# return student id in Student table
		get_student_id=self.session.query(Student).filter(Student.id==student_id).one()
			
		# Check if parameters have been supplied
		if student_id and class_id:
			# Check if a class has started and student has not attended any other class
			if get_class_id.class_in_session==True and get_student_id.is_student_in_class==False:				
				check_in_student = TrackStudent(student_id=student_id,class_id=class_id,check_in_time=now)
				get_student_id.is_student_in_class=True
				self.session.add(check_in_student)
				self.session.commit()
				click.secho("Checked in student '{}' into class '{}'".format(student_id,class_id), fg='green')
			elif get_class_id.class_in_session==False:
				# Reset is_student_in_class to False if the Class has ended
				get_student_id.is_student_in_class=False
				self.session.commit()
				click.secho("Warning! Class {} has not started.".format(class_id), fg='red')
			else:
				click.secho("Warning! You can only check into a single class.".format(class_id), fg='red')

	def check_out(self,student_id,class_id,reason):
		"""Checks out a student from a class at the current time.
		"""
		# Check current time
		now = datetime.now()
		# return class id in Class table
		get_class_id=self.session.query(Class).filter(Class.id==class_id).one()
		
		# return student id in Student table
		get_student_id=self.session.query(Student).filter(Student.id==student_id).one()

		# return the tracked student id in TrackStudent table
		get_tracked_student_id=self.session.query(TrackStudent).filter(TrackStudent.student_id==student_id).one()
			
		# Check if parameters have been supplied
		if student_id and class_id and reason:
			# Check if a class has started and student is in a class
			if get_class_id.class_in_session==True and get_student_id.is_student_in_class==True:				
				#check_in_student = TrackStudent(student_id=student_id,class_id=class_id,check_in_time=now)
				get_tracked_student_id.check_out_time=now
				get_tracked_student_id.reason=reason
				get_student_id.is_student_in_class=False
				self.session.commit()
				click.secho("Checked out student '{}' from class '{}'".format(student_id,class_id), fg='green')
			# Check if student is in any class
			elif get_student_id.is_student_in_class==False:
				click.secho("Warning! Student {} is not in any class.".format(student_id), fg='red')
			else:
				click.secho("Warning! [student_id] [class_id] [reason] cannot be empty.", fg='red')

	def student_list(self):
		"""Lists all students
		"""
		# Create an instance of the PrettyTable
		x = PrettyTable()

		# Fetch all rows in Student table
		get_students=self.session.query(Student).order_by(desc(Student.is_student_in_class))		
		
		# Label the Table Columns
		x.field_names = ["Student ID","Student Name","Checked In"]
		
		# Loop through the rows
		for i in get_students:
			x.add_row([i.id,i.name,i.is_student_in_class])			
		print(x)

if __name__ == '__main__':
	Database().cmdloop()
