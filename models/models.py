from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
	"""Creates student table"""

	__tablename__ = 'student'
	id = Column(Integer,primary_key=True)
	name = Column(String(50))
    
class Class(Base):
	"""Creates class table"""

	__tablename__ = 'class'
	id = Column(Integer,primary_key=True)
	name = Column(String(50))
	status = Column(Boolean, default=False)
	class_start_time = Column(DateTime)
	class_end_time = Column(DateTime)