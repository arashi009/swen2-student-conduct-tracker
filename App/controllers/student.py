from App.database import db
from App.models.student import Student
from sqlalchemy.exc import SQLAlchemyError


def get_student_by_full_name(firstname: str, lastname: str):
    existing_student = Student.query.filter_by(firstname=firstname, lastname=lastname).first()
    return None if existing_student is None else existing_student


def get_student_by_id(id: int):
    existing_student = Student.query.filter_by(student_id=id).first()
    return None if existing_student is None else existing_student


def create_student(firstname, lastname, programme):
    try:
        new_student = Student(firstname, lastname, programme)
        db.session.add(new_student)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print("Student could not be added")


def query_student_by_name(firstname, lastname):
    students = Student.query.filter_by(firstname=firstname, lastname=lastname).all()
    return students


def get_all_students():
    students = Student.query.all()
    return students
