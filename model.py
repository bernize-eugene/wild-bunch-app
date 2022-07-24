"""Models for Wild Bunch App"""

from datetime import datetime
from flask_sqlalchemu import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    user_location_id = db.Column(
        db.Integer, db.ForeignKey("user_location.user_location_id"))
    user_event_id = db.Column(
        db.Integer, db.ForeignKey("user_event.user_event_id"))

    def __repr__(self):
        return (
            f"user_id = {self.user_id}\n"
            f"first_name = {self.first_name}\n"
            f"last_name = {self.last_name}\n"
            f"email = {self.email}\n"
            f"phone = {self.phone}\n"
            f"username = {self.username}\n"
            f"password = {self.password}\n"
            f"user_location_id = {self.user_location_id}\n"
            f"user_event_id = {self.user_event_id}"
        )


"""Database Connection"""


def connect_to_db(flask_app, db_uri="+++++++++++++++", echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ = "__main__":
    from server import app
