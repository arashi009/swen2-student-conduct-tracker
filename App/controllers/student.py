from prettytable import PrettyTable
from App.database import db
from App.models.student import Student
from sqlalchemy.exc import SQLAlchemyError


def get_student_by_full_name(first_name: str, last_name: str):
    existing_student = Student.query.filter_by(first_name=first_name, last_name=last_name).first()
    return None if existing_student is None else existing_student


def get_student_by_id(id: int):
    existing_student = Student.query.filter_by(id=id).first()
    return None if existing_student is None else existing_student


def create_student(first_name, last_name, programme):
    try:
        new_student = Student(first_name, last_name, programme)
        db.session.add(new_student)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print("Student could not be added")


def query_student_by_name(first_name, last_name):
    students = Student.query.filter_by(first_name=first_name, last_name=last_name).all()
    return students


def get_all_students():
    students = Student.query.all()
    return students


# def create_student_table(students):
#     table = PrettyTable()
#     table.field_names = [
#         "Student ID",
#         "Name",
#         "Programme",
#     ]

#     for student in students:
#         table.add_row([student.id, f"{student.first_name} {student.last_name}", student.programme])

#     print(table)
