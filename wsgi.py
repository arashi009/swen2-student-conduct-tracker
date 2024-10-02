# import click
from flask.cli import AppGroup
from App.database import get_migrate
from App.main import create_app
from App.controllers import initialize
from App.controllers.student import (
    create_student,
    get_all_students,
    get_student_by_id,
    get_students_by_name,
)
from App.controllers.staff import (
    get_all_staff,
    get_staff_by_id,
    get_staff_by_name,
)
from models.staff import Staff
from models.student import Student

# from App.controllers.review import create_review_table

app = create_app()
migrate = get_migrate(app)


@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print("database intialized")


"""
Reviewer Commands
"""
reviewer = AppGroup(
    "reviewer", help="reviewer commands for viewing students and reading/writing review"
)


@reviewer.command("add_student", help="adds a new student to the database")
def add() -> None:
    first_name = input("Student First Name: ")
    last_name = input("Student Last Name: ")
    programme = input("Student Programme: ")
    print(f"Student {first_name} was added!")


@reviewer.command(
    "find_students", help="lists all students with the specified first and last name"
)
def find_student() -> None:

    first_name = input("Student First Name: ")
    last_name = input("Student Last Name: ")
    students = get_students_by_name(first_name, last_name)
    if not students:
        print("No students found")
        return


@reviewer.command(
    "find_staff", help="lists all staff with the specified first and last name"
)
def find_staff() -> None:
    first_name = input("Staff Member First Name: ")
    last_name = input("Staff Member Last Name: ")
    staff = get_staff_by_name(first_name, last_name)
    if not staff:
        print("No staff found")
        return


@reviewer.command("list_students", help="lists all students in the database")
def list_students():
    students = get_all_students()
    if not students:
        print("Currently No Students in the Database")
        return


@reviewer.command("list_staff", help="lists all staff in the database")
def list_staff():
    staff = get_all_staff()
    if not staff:
        print("Currently No staff in the Database")
        return


@reviewer.command("review_student", help="creates a review of a student")
def write_review() -> None:
    id: str = input("Enter the ID of the student you would like to review: ")
    score: int = int(input("Enter their score out of 10: "))
    comment: str = input("Make a comment about the student: ")

    if score > 10:
        print("Score should be a value from 0 to 10")
        return

    student: Student | None = get_student_by_id(id)
    if student is None:
        print(f"Student could not be found")
        return

    id: str = input("Enter your staff id: ")
    staff: Staff | None = get_staff_by_id(id)
    if staff:
        try:
            staff.review_student(score, comment, id)
            print("Review added successfully")
        except ValueError as e:
            print(f"Error: {str(e)}")
    else:
        print("Invalid staff username")


@reviewer.command(
    "get_student_reviews", help="lists the reviews for a student listed by ID"
)
def get_student_reviews() -> None:
    id: str = input("Enter Student ID: ")
    student: Student | None = get_student_by_id(id)
    if student is None:
        print(f"{id} is not a valid student ID")
        return
    reviews = student.reviews
    if not reviews:
        print(f"Student of ID:{student.id} currently has no reviews")
        return


@reviewer.command(
    "get_staff_reviews", help="lists the reviews written by a staff member by username"
)
def review() -> None:
    id: str = input("Enter Staff ID: ")
    staff: Staff | None = get_staff_by_id(id)
    if staff is None:
        print(f"{id} is not a valid member of staff")
        return
    reviews = staff.reviews
    if not reviews:
        print(f"{staff.first_name} {staff.last_name} has not written any reviews")
        return


app.cli.add_command(reviewer)
