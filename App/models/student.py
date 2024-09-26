from typing import Any
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Student(db.Model):
    student_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    programme: Any = db.Column(db.String, nullable=False)
    num_reviews = db.Column(db.Integer, nullable=False)
    reviews = db.relationship("Review", backref="student")

    def __init__(self, firstname, lastname, programme):
        self.firstname = firstname
        self.lastname = lastname
        self.programme = programme
        self.num_reviews = 0

    def __repr__(self):
        return f"========Student========\nID:{self.student_id}\nName: {self.firstname} {self.lastname}\nProgramme:{self.programme}\nReviews:{self.num_reviews}"
