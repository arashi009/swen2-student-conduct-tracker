from App.database import db
from App.models.student import Student


class Review(db.Model):
    reviewID: int = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    student_id: int = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)
    score: int = db.Column(db.Integer, nullable=False)
    comment: str = db.Column(db.String, nullable=True)
    experience: bool = db.Column(db.Boolean, nullable=False)

    def __init__(self, student_id: int, score: int, comment: str) -> None:
        # self.reviewID = reviewID
        self.score = score
        self.student_id = student_id
        self.comment = comment
        student = Student.query.filter_by(student_id=student_id).first()
        student.num_reviews += 1
        self.experience = False if self.score < 5 else True

    def __repr__(self) -> str:
        student = Student.query.filter_by(student_id=self.student_id).first()
        student_fullname = f"{student.firstname} {student.lastname}"
        return f"Conduct Review of Student [{self.student_id},{student_fullname}]:\nRating: {self.score}/10\ncomment: {self.comment}\nExperience with Student:{" Positive" if self.experience else " Negative"}\n"

