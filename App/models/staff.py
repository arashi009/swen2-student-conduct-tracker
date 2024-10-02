from werkzeug.security import check_password_hash
from App.database import db
from App.models.user import User


class Staff(User):
    id: str = db.Column(db.String(9), db.ForeignKey("user.id"), primary_key=True)
    first_name: str = db.Column(db.String(50), nullable=False)
    last_name: str = db.Column(db.String(50), nullable=False)
    title: str = db.Column(db.String(50), nullable=False)
    reviews = db.relationship("Review", backref="staff")

    def __init__(self, id, first_name, last_name, title, password) -> None:
        super().__init__(id, password)
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.title: str = title

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.title})"

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)
