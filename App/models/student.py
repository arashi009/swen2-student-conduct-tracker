from typing import Any
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Student(db.Model):
    id: str = db.Column(db.String(9), nullable=False, primary_key=True, autoincrement=True)
    first_name: str = db.Column(db.String(100), nullable=False)
    last_name: str = db.Column(db.String(100), nullable=False)
    programme: str = db.Column(db.String(100), nullable=False)
    reviews = db.relationship("Review", backref="student")

    def __init__(self, first_name: str, last_name: str, programme: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme

    def __repr__(self) -> str:
        return f"Student[ID:{self.id}, Name: {self.first_name} {self.last_name}, Programme:{self.programme}, Reviews:{self.reviews.length}]"
