""" Database Architecture """
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
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
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    user_type = Column(String, nullable=False)
    gender = Column(String, nullable=False)

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
    name = Column(String, nullable=False)
    hostel_id = Column(Integer, nullable=False)


# Create the database tables (only needed once)
Base.metadata.create_all(engine)
