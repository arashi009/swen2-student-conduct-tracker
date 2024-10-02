from App.models.staff import Staff
from App.database import db
from sqlalchemy.exc import SQLAlchemyError


def create_staff(id, first_name, last_name, password) -> Staff | None:
    try:
        staff = Staff(id, password, first_name, last_name)
        db.session.add(staff)
        db.session.commit()
        return Staff
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"{e}")
        return None


def get_staff_by_id(id: str) -> Staff | None:
    return Staff.query.filter_by(id=id).first()


def delete_staff_by_id(id: str) -> Staff | None:
    staff = Staff.query.filter_by(id=id).first()
    try:
        db.session.delete(staff)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Could not delete staff {id} from the system; {e}")


def get_staff_by_name(first_name, last_name):
    return Staff.query.filter_by(first_name=first_name, last_name=last_name).all()


def get_all_staff():
    return Staff.query.all()


# def get_staff_by_username(username):
#     return Staff.query.filter_by(username=username).first()
