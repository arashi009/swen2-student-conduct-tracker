from App.database import db
from App.models.student import Student


class Review(db.Model):
    __tablename__ = "review"

    reviewID = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    staff_id = db.Column(db.Integer, db.ForeignKey("staff.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=True)
    experience = db.Column(db.Boolean, nullable=False)

    # Define relationships
    student = db.relationship("Student", back_populates="reviews")
    staff = db.relationship("Staff", back_populates="reviews")

    def __init__(self, student_id: int, score: int, comment: str, staff) -> None:
        self.student_id = student_id
        self.score = score
        self.staff = staff
        self.comment = comment
        self.experience = False if self.score < 5 else True

    def __repr__(self) -> str:
        student = Student.query.filter_by(id=self.student_id).first()
        student_fullname = f"{student.firstname} {student.lastname}" if student else "Unknown Student"
        return (
            f"Conduct Review of Student [{self.student_id}, {student_fullname}]:\n"
            f"Rating: {self.score}/10\n"
            f"Comment: {self.comment}\n"
            f"Experience with Student: {'Positive' if self.experience else 'Negative'}\n"
        )
