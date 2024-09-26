from App.database import db
from App.models.student import Student


def get_student_by_full_name(firstname: str, lastname: str):
    existing_student = Student.query.filter_by(firstname=firstname, lastname=lastname).first()
    return None if existing_student is None else existing_student


def get_student_by_id(id: int):
    existing_student = Student.query.filter_by(student_id=id).first()
    return None if existing_student is None else existing_student


def add_student(firstname, lastname, programme):
    new_student = Student(firstname, lastname, programme)
    db.session.add(new_student)
    db.session.commit()


def query_student_by_name(firstname, lastname):
    students = Student.query.filter_by(firstname=firstname, lastname=lastname).all()
    return students


def get_all_students():
    students = Student.query.all()
    return students
