import csv
from App.controllers.student import create_student
from App.controllers.staff import create_staff
from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user("bob", "bobpass")
    with open("students.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            create_student(row["firstname"], row["lastname"], row["programme"])

    with open("staff.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            create_staff(row["firstname"], row["lastname"], row["title"], row["password"])

    # make staff write a review
