# import click
from flask.cli import AppGroup
from App.database import get_migrate
from App.main import create_app
from App.controllers import initialize
from App.controllers.student import (
    create_student,
    get_all_students,
    get_student_by_id,
    query_student_by_name,
)
from App.controllers.staff import get_all_staff, get_staff_by_name, get_staff_by_username
from App.controllers.review import create_review_table

app = create_app()
migrate = get_migrate(app)


@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print("database intialized")


"""
Reviewer Commands
"""
reviewer = AppGroup("reviewer", help="reviewer commands for viewing students and reading/writing review")


@reviewer.command("add_student", help="adds a new student to the database")
def add() -> None:
    first_name = input("Student First Name: ")
    last_name = input("Student Last Name: ")
    programme = input("Student Programme: ")
    create_student(first_name, last_name, programme)
    print(f"Student {first_name} was added!")


@reviewer.command("find_students", help="lists all students with the specified first and last name")
def find_student() -> None:

    first_name = input("Student First Name: ")
    last_name = input("Student Last Name: ")
    students = query_student_by_name(first_name, last_name)
    if not students:
        print("No students found")
        return
    # else:
    # create_student_table(students)


@reviewer.command("find_staff", help="lists all staff with the specified first and last name")
def find_staff() -> None:
    first_name = input("Staff Member First Name: ")
    last_name = input("Staff Member Last Name: ")
    staff = get_staff_by_name(first_name, last_name)
    if not staff:
        print("No staff found")
        return
    # else:
    # create_staff_table(staff)


@reviewer.command("list_students", help="lists all students in the database")
def list_students():
    students = get_all_students()
    if not students:
        print("Currently No Students in the Database")
        return
    # else:
    #     create_student_table(students)


@reviewer.command("list_staff", help="lists all staff in the database")
def list_staff():
    staff = get_all_staff()
    if not staff:
        print("Currently No staff in the Database")
        return
    # else:
    # create_staff_table(staff)


@reviewer.command("review_student", help="creates a review of a student")
def write_review() -> None:
    student_id = int(input("Enter the ID of the student you would like to review: "))
    score = int(input("Enter their score out of 10: "))
    comment = input("Make a comment about the student: ")

    if score > 10:
        print("Score should be a value from 0 to 10")
        return

    student = get_student_by_id(student_id)
    if student is None:
        print(f"Student could not be found")
        return

    username = input("Enter your staff username: ")
    staff = get_staff_by_username(username)
    if staff:
        try:
            staff.review_student(score, comment, int(student_id))
            print("Review added successfully")
        except ValueError as e:
            print(f"Error: {str(e)}")
    else:
        print("Invalid staff username")


@reviewer.command("get_student_reviews", help="lists the reviews for a student listed by ID")
def get_student_reviews() -> None:
    student_id = int(input("Enter Student ID: "))
    student = get_student_by_id(student_id)
    if student is None:
        print(f"{student_id} is not a valid student ID")
        return

    reviews = student.reviews
    if not reviews:
        print(f"Student of ID:{student.student_id} currently has no reviews")
        return

    create_review_table(reviews)


@reviewer.command("get_staff_reviews", help="lists the reviews written by a staff member by username")
def review() -> None:
    username = input("Enter Staff Username: ")
    staff = get_staff_by_username(username)
    if staff is None:
        print(f"{username} is not a valid member of staff")
        return
    reviews = staff.reviews
    if not reviews:
        print(f"{staff.first_name} {staff.last_name} has not written any reviews")
        return
    else:
        create_review_table(reviews)


app.cli.add_command(reviewer)


# @reviewer.command("add_student", help="adds a new student to the database")
# @click.argument("first_name", type=str)
# @click.argument("last_name", type=str)
# @click.argument("programme", type=str)
# def add(first_name: str, last_name: str, programme: str) -> None:
#     create_student(first_name, last_name, programme)
#     print(f"Student {first_name} was added!")

# @reviewer.command("review_student", help="creates a review of a student")
# @click.argument("student_id")
# @click.argument("score")
# @click.argument("comment")
# def write_review(student_id, score: int, comment) -> None:
#     score = int(score)
#     if score > 10:
#         print("Score should be a value from 0 to 10")
#         return
#     student = get_student_by_id(student_id)
#     if student is None:
#         print(f"Student could not be found")
#         return
#     username = input("Enter your staff username: ")
#     staff = get_staff_by_username(username)
#     if staff:
#         try:
#             staff.review_student(score, comment, int(student_id))
#             print("Review added successfully")
#         except ValueError as e:
#             print(f"Error: {str(e)}")
#     else:
#         print("Invalid staff username")
# @reviewer.command("get_student_reviews", help="lists the reviews for a student listed by ID")
# def get_student_reviews() -> None:
#     student_id = int(input("Enter Student ID: "))
#     student = get_student_by_id(student_id)
#     if student is None:
#         print(f"{student_id} is not a valid student ID")
#         return
#     review = student.reviews
#     if not review:
#         print(f"Student of ID:{student.student_id} currently has no reviews")
#         return
#     print(f"===================Reviews for {student.first_name}===================")
#     for review in review:
#         print(review)
