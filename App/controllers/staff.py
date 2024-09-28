from App.models.staff import Staff
from App.database import db
from sqlalchemy.exc import SQLAlchemyError


def create_staff(firstname, lastname, title, password):
    try:
        staff = Staff(firstname, lastname, title, password)
        db.session.add(staff)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error adding staff member {firstname} {lastname}: {e}")


def get_staff_by_id(staff_id: int):
    return Staff.query.filter_by(id=staff_id).first()


def get_staff_by_name(firstname, lastname):
    return Staff.query.filter_by(firstname=firstname, lastname=lastname).first()


def get_staff_by_title(title):
    return Staff.query.filter_by(title=title).all()


def get_staff_by_username(username):
    return Staff.query.filter_by(username=username).first()


def get_all_staff():
    return Staff.query.all()
