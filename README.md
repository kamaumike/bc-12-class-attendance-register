# bc-12-class-attendance-register
Class Attendance Register app

__C.A.R__ stands for Class Attendance Register.It's a Command Line Application written in Python 3 using [SQLite](https://sqlite.org/download.html SQLite database).The appplication is used to check-in students when they come into a class.

## Implemented Features
- Add a student
- Delete a student
- Add a class
- Delete a class
- Start a class
- End a class
- List all students
- List all classes
- Check in a student into a class
- Check out a student from a class 


## Unimplemented Features

- Show the status of the class and the number of students in that class at the moment


## Installation & Configurations

__Prerequisites__

1. You should install Python version 3.5.2.

2. It is recommended that you use a virtual environment for this project.

3. Create a [Github account](https://github.com/)

4. Install [Git](https://git-scm.com/downloads) 

5. Clone this repository
`https://github.com/kamaumike/bc-12-class-attendance-register/tree/develop`

6. Install requirements `pip install -r requirements.txt`

7. Move into the `bc-12-class-attendance-register directory`

8. Open your terminal and type `alembic init migrations` command

9. Locate the `alembic.ini` file and replace line 32 with `sqlalchemy.url = sqlite:///classregister.db`

10. Locate the `migrations` directory and inside it locate the `env.py` file.

11. In the `env.py` file add these configurations after line 4
	On line 5 add `import sys`
	On line 6 add '# Add path to search for files to import`
	On line 7 add `sys.path.insert(0, './models')`
	On line 8 add `from models import Base`

12. Locate `target_metadata = None` and replace it with `target_metadata = Base.metadata`

13. Run `alembic revision --autogenerate` command

14. Run `alembic upgrade head` command

7. Run `python app.py`
