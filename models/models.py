from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Student(Base):
	"""Creates student table"""

	__tablename__ = 'student'
	id = Column(Integer,primary_key=True)
	name = Column(String(50))
    