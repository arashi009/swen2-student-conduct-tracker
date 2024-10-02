import csv
from venv import create
from App.controllers.student import create_student
from App.controllers.staff import create_staff, get_staff_by_name, get_staff_by_username

from App.models.staff import Staff
from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    with open("data/students.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            create_student(row["firstname"], row["lastname"], row["programme"])

    with open("staff.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            create_staff(row["firstname"], row["lastname"], row["title"], row["password"])

    with open("data/reviews.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            create_review(
                int(row["score"]),
                row["comment"],
                int(row["student_id"]),
                Staff.query.filter_by(id=row["staff_id"]).first(),
            )
