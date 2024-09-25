import click
from flask.cli import AppGroup
from App.database import get_migrate
from App.main import create_app
from App.controllers import initialize
from App.controllers.student import add_student, get_all_students, get_student_by_id, query_student_by_name
from App.controllers.review import add_review

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
@click.argument("firstname", type=str)
@click.argument("lastname", type=str)
def add(firstname: str, lastname: str) -> None:
    add_student(firstname, lastname)
    print(f"Student {firstname} was added!")


@reviewer.command("find_students", help="lists all students with the specified first and last name")
@click.argument("firstname")
@click.argument("lastname")
def find(firstname, lastname) -> None:
    students = query_student_by_name(firstname, lastname)
    if students is None:
        print("No students found")
        return
    for student in students:
        print(student)
    print("==========================")


@reviewer.command("list_students", help="lists all students in the database")
def list_students():
    students = get_all_students()
    if not students:
        print("Currently No Students in the Database")
        return
    for student in students:
        print(student)


@reviewer.command("review_student", help="creates a review of a student")
@click.argument("student_id")
@click.argument("score")
@click.argument("comment")
def write_review(student_id, score: int, comment) -> None:
    score = int(score)
    if score > 10:
        print("Score should be a value from 0 to 10")
    student = get_student_by_id(student_id)
    if student is None:
        print(f"Student could not be found")
        return
    else:
        add_review(score, comment, student)
        print(f"review posted!")


@reviewer.command("get_reviews", help="lists the reviews for a student listed by ID")
@click.argument("student_id")
def review(student_id) -> None:
    student = get_student_by_id(student_id)
    if student is None:
        print(f"{student_id} is not a valid student ID")
        return
    review = student.reviews
    if not review:
        print(f"Student of ID:{student.student_id} currently has no reviews")
        return
    print(f"===================Reviews for {student.firstname}===================")
    for review in review:
        print(review)


app.cli.add_command(reviewer)
