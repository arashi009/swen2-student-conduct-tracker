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


def get_student_by_full_name(first_name: str, last_name: str) -> Student | None:
    student: Student = Student.query.filter_by(first_name=first_name, last_name=last_name).first()
    return student


def get_student_by_id(id: str) -> Student | None:
    existing_student = Student.query.filter_by(id=id).first()
    return existing_student


def get_students_by_name(first_name: str, last_name: str):
    students = Student.query.filter_by(first_name=first_name, last_name=last_name).all()
    return students


def get_all_students():
    students = Student.query.all()
    return students


def delete_student(id: str) -> bool:
    try:
        student = get_student_by_id(id)
        if student:
            db.session.delete(student)
            db.session.commit()
            return True
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
    return False


def get_students_by_programme(programme: str):
    return Student.query.filter_by(programme=programme).all()
