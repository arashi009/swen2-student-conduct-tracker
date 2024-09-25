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
