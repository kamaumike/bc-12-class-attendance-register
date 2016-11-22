import cmd
from class_register import Database

class AttendanceRegister(cmd.Cmd):
	"Class Attendance Register"

	def do_student_add(self,name):
		"""student_add [name]
		Add the name of a student
		"""
		db = Database()
		db.student_add(name)

if __name__ == '__main__':
	AttendanceRegister().cmdloop()


