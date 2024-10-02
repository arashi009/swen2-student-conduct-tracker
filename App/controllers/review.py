from App.database import db
from App.models.review import Review
from sqlalchemy.exc import SQLAlchemyError


def create_review(student_id, staff_id, rating, comment) -> Review | None:
    # student = Student.query.get(student_id)
    # if student is None:
    # raise ValueError(f"No student found with ID {student_id}")
    try:
        review = Review(student_id, staff_id, rating, comment)
        db.session.add(review)
        db.session.commit()
        return Review
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"{e}")
        return None


def get_review_by_id(id) -> Review | None:
    return Review.query.filter_by(id=id).first()


# not sure if to add def get_staff_reviews(id) since it could just be accessed through a Staff Instance


def delete_review(id) -> None:
    review: Review | None = get_review_by_id(id)
    try:
        db.session.delete(review)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"{e}")
