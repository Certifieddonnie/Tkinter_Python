""" Authentication module for Hostel Management System """
import bcrypt

from Hostel_Management.database import User, Student
# from Hostel_Management.session import Session


# login function
def login(username, password):
    """ Login function """
    user = User.get_user(user_name=username)

    if user:
        db_pwd = user.password
        password = password.encode('utf-8')

        if bcrypt.checkpw(password=password, hashed_password=db_pwd):
            return user

    return None


def register(first_name, last_name, user_name, password, user_type, gender):
    """ Register Function """
    existing_user = User.get_user(user_name=user_name)

    if existing_user:
        return "true"

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(first_name, last_name, user_name,
                    hashed_password, user_type, gender)

    new_user.create()


def sign_student(name, hostel_id):
    """ Store Student data and hostel id in a table """
    new_student = Student(name, hostel_id)

    new_student.create()


def change_password(user, old_password, new_password):
    """ Change user password """
    if user:
        usr_pwd = user.password
        old_password = old_password.encode('utf-8')

        if bcrypt.checkpw(old_password, usr_pwd):
            hashed_password = bcrypt.hashpw(
                new_password.encode('utf-8'), bcrypt.gensalt())

            # Update password
            user.password = hashed_password
            user.update()

    return 'error'
