from App.database import db
from App.models.review import Review
from App.models.student import Student


def create_review(student_id, staff_id, rating, comment) -> None:
    student = Student.query.get(student_id)
    if student is None:
        raise ValueError(f"No student found with ID {student_id}")
    review = Review(student_id, staff_id, rating, comment)
    db.session.add(review)
    db.session.commit()
