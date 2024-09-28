from App.models.review import Review
from App.database import db
from App.models.student import Student


def add_review(score: int, comment: str, student_id: int, staff) -> None:
    student = Student.query.get(student_id)
    if student is None:
        raise ValueError(f"No student found with ID {student_id}")

    review = Review(student_id=student_id, score=score, comment=comment, staff=staff)
    student.num_reviews += 1
    db.session.add(review)
    db.session.commit()
