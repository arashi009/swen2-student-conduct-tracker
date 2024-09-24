from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Student(db.Model):
    student_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    num_reviews = db.Column(db.Integer, nullable=False)
    reviews = db.relationship("Review", backref="student")

    def __init__(
        self,
        firstname,
        lastname,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.num_reviews = 0

    def __repr__(self):
        return f"========Student========\nID:{self.student_id}\nName: {self.firstname} {self.lastname}\nReviews:{self.num_reviews}"


def get_student_by_full_name(firstname: str, lastname: str):
    existing_student = Student.query.filter_by(firstname=firstname, lastname=lastname).first()
    return None if existing_student is None else existing_student


def get_student_by_id(id: int):
    existing_student = Student.query.filter_by(student_id=id).first()
    return None if existing_student is None else existing_student
