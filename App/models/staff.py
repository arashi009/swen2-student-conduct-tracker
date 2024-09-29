from prettytable import PrettyTable
from sqlalchemy import Nullable
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models.user import User
from App.models.review import Review


class Staff(User):
    __tablename__ = "staff"
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    reviews_written = db.Column(db.Integer, nullable=False)
    reviews = db.relationship("Review", back_populates="staff")

    def __init__(self, firstname, lastname, title, password):
        unique_username = f"{firstname.lower()}.{lastname.lower()}"
        super().__init__(unique_username, password)
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.reviews_written = 0

    def __repr__(self):
        return f"========Staff========\nID: {self.id}\nUsername: {self.username}\nName: {self.firstname} {self.lastname}\nReviews Written: {self.reviews_written}"

    def get_json(self):
        json_data = super().get_json()
        json_data.update(
            {"firstname": self.firstname, "lastname": self.lastname, "reviews_written": self.reviews_written}
        )
        return json_data

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def review_student(self, score: int, comment: str, student_id: int) -> None:
        review = Review(student_id, score, comment, self)
        self.reviews_written += 1
        db.session.add(review)
        db.session.commit()


def create_staff_table(staff):
    table = PrettyTable()
    table.field_names = ["ID", "Title", "Name", "Username", "Reviews Written"]

    for member in staff:
        table.add_row(
            [member.id, member.title, f"{member.firstname} {member.lastname}", member.username, member.reviews_written]
        )
    print(table)
