from prettytable import PrettyTable
from App.database import db
from App.models.review import Review
from App.models.student import Student


def add_review(score: int, comment: str, student_id: int, staff) -> None:
    student = Student.query.get(student_id)
    if student is None:
        raise ValueError(f"No student found with ID {student_id}")

    review = Review(student_id=student_id, score=score, comment=comment, staff=staff)
    student.num_reviews += 1
    db.session.add(review)
    db.session.commit()


def create_review_table(reviews):
    table = PrettyTable()
    table.field_names = ["Review ID", "Student Name", "Score", "Comment", "Experience", "Written by"]
    for review in reviews:
        experience = "Positive" if review.experience else "Negative"
        staff_name = f"{review.staff.firstname} {review.staff.lastname}"
        student_name = f"{review.student.firstname} {review.student.lastname}"
        table.add_row([review.reviewID, student_name, review.score, review.comment, experience, staff_name])
    print(table)

def review_student(self, score: int, comment: str, student_id: int) -> None:
    review = Review(student_id, score, comment, self)
    self.reviews_written += 1
    db.session.add(review)
    db.session.commit()
