import csv
from venv import create
from App.controllers.student import create_student
from App.controllers.staff import create_staff, get_staff_by_name, get_staff_by_username
from App.controllers.review import add_review
from App.models.staff import Staff
from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    staff: Staff
    create_user("bob", "bobpass")
    with open("students.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            create_student(row["firstname"], row["lastname"], row["programme"])

    with open("staff.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            create_staff(row["firstname"], row["lastname"], row["title"], row["password"])

    with open("reviews.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            add_review(
                int(row["score"]),
                row["comment"],
                int(row["student_id"]),
                Staff.query.filter_by(id=row["staff_id"]).first(),
            )
    # add_review(1, "Well mannered student", 3, Staff.query.filter_by(id=2).first())
    # add_review(2, "Well mannered", 7, Staff.query.filter_by(id=3).first())
    # add_review(3, "Goated", 5, Staff.query.filter_by(id=4).first())
    # add_review(4, "Goated", 6, Staff.query.filter_by(id=5).first())
    # add_review(5, "Attends classes irregularly", 12, Staff.query.filter_by(id=6).first())
    # add_review(6, "Attends classes irregularly", 12, Staff.query.filter_by(id=7).first())
    # add_review(7, "Attends classes irregularly", 12, Staff.query.filter_by(id=8).first())

    # make staff write a review
