from App.models.review import Review
from App.database import db


def add_review(score, comment, student, staff):
    review = Review(student.student_id, score=score, comment=comment, staff=staff)
    student.num_reviews += 1
    staff.reviews_written += 1
    db.session.add(review)
    db.session.commit()
