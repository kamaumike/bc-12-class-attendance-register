import cmd
import click
from class_register import Database

class AttendanceRegister(cmd.Cmd):
	"Class Attendance Register"

	def do_student_add(self,name):
		"""student_add [name]
		Add the name of a student
		"""
		db = Database()
		db.student_add(name)

	def do_student_remove(self,student_id):
		"""student_remove [student_id]
		Accepts a student id
		"""
		db = Database()
		db.student_remove(student_id)

	def do_class_add(self,name):
		"""class_add [name]
		Add the name of a class
		"""
		db = Database()
		db.class_add(name)

	def do_class_remove(self,class_id):
		"""class_remove [class_id]
		Accepts a class id
		"""
		db = Database()
		db.class_remove(class_id)


	def do_log_start(self,class_id):
		"""log_start [class_id]
		Accepts a class id
		"""	
		db = Database()
		db.log_start(class_id)

	def do_log_end(self,class_id):
		"""log_end [class_id]
		Accepts a class id
		"""	
		db = Database()
		db.log_end(class_id)

	def do_check_in(self,args):
		"""check_in [student_id][class_id]
		Accepts a student id and class id
		"""
		data=args.split()
		db = Database()
		db.check_in(data[0],data[1])

	def do_check_out(self,args):
		"""check_in [student_id][class_id][reason]
		Accepts a student id ,class id and reason
		"""
		data=args.split()
		db = Database()
		db.check_out(data[0],data[1],data[2])
		
	def do_student_list(self, args):
		"""[student_list]
		Lists all students
		"""	
		db = Database()
		db.student_list()

	def do_class_list(self, args):
		"""[class_list]
		Lists all classes
		"""	
		db = Database()
		db.class_list()		

	def do_exit(self,exit):
		"""exit
		Exits the application
		"""
		click.clear()
		return True
		
if __name__ == '__main__':
	AttendanceRegister().cmdloop()
