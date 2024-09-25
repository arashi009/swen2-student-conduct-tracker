from App.models.review import Review
from App.database import db


def add_review(score, comment, student):
    review = Review(student.student_id, score=score, comment=comment)
    db.session.add(review)
    db.session.commit()
