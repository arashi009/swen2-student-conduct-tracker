from App.database import db
from App.models.student import Student
from sqlalchemy.exc import SQLAlchemyError


def create_student(id, first_name, last_name, programme) -> Student | None:
    try:
        student = Student(id, first_name, last_name, programme)
        db.session.add(student)
        db.session.commit()
        return student
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None


def get_student_by_full_name(first_name: str, last_name: str) -> Student:
    student: Student = Student.query.filter_by(
        first_name=first_name, last_name=last_name
    ).first()
    if student is None:
        return None
    return student


def get_student_by_id(id: int):
    existing_student = Student.query.filter_by(id=id).first()
    return None if existing_student is None else existing_student


def query_student_by_name(first_name, last_name):
    students = Student.query.filter_by(first_name=first_name, last_name=last_name).all()
    return students


def get_all_students():
    students = Student.query.all()
    return students
