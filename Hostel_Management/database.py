""" Database Architecture """
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PWD = os.getenv("MYSQL_PWD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")


# Create a database engine and session
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                       format(MYSQL_USER,
                              MYSQL_PWD,
                              MYSQL_HOST,
                              MYSQL_DB))
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define your database model classes


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    user_name = Column(String(120), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    user_type = Column(String(20), nullable=False)
    gender = Column(String(20), nullable=False)

    def __init__(self, first_name, last_name, user_name, password, user_type, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.user_type = user_type
        self.gender = gender

    def create(self):
        session.add(self)
        session.commit()

    @classmethod
    def get_user(cls, user_name):
        return session.query(cls).filter_by(user_name=user_name).first()

    def update(self):
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    hostel_id = Column(Integer, ForeignKey('hostels.id'))
    hostel = relationship("Hostel", back_populates="students")

    def __init__(self, name, hostel_id):
        self.name = name
        self.hostel_id = hostel_id

    def create(self):
        session.add(self)
        session.commit()

    @classmethod
    def get_students_by_hostel_id(cls, hostel_id):
        return session.query(cls).filter_by(hostel_id=hostel_id).all()

    def update(self):
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()


class Hostel(Base):
    __tablename__ = 'hostels'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)

    students = relationship("Student", back_populates="hostel")


# Create the database tables (only needed once)
Base.metadata.create_all(engine)
