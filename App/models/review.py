from App.database import db
from App.models.student import Student
from App.models import student


class Review(db.Model):
    __tablename__ = "review"

    reviewID: int = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    staff_id: int = db.Column(db.Integer, db.ForeignKey("staff.id"), nullable=False)
    student_id: int = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)
    score: int = db.Column(db.Integer, nullable=False)
    comment: str = db.Column(db.String, nullable=False)
    experience: bool = db.Column(db.Boolean, nullable=False)

    student = db.relationship("Student", back_populates="reviews")
    staff = db.relationship("Staff", back_populates="reviews")

    def __init__(self, student_id: int, score: int, comment: str, staff) -> None:
        self.score = score
        self.student_id = student_id
        self.staff = staff
        self.comment = comment
        self.experience = score >= 5

    def __repr__(self) -> str:
        student: Student = Student.query.filter_by(student_id=self.student_id).first()
        student_fullname: str = f"{student.firstname} {student.lastname}" if student else "Unknown Student"

        review_details = (
            f"Conduct Review of Student [{self.student_id}, {student_fullname}]:\n"
            f"Rating: {self.score}/10\n"
            f"Comment: {self.comment}\n"
            f"Experience with Student: {'Positive' if self.experience else 'Negative'}\n"
            f"Review Written by: {self.staff.firstname} {self.staff.lastname}"
        )

        return review_details
