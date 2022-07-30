"""Models for Wild Bunch App"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

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


class User_Location(db.Model):
    """User location longitude and latitude coordinates"""

    __tablename__ = "user_location"

    user_location_id = db.Column(
        db.Integer, autoincrement=True, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    def __repr__(self):
        return (
            f"user_location_id = {self.user_location_id}\n"
            f"longitude = {self.longitude}\n"
            f"latitude = {self.latitude}"

        )


class User_Event(db.Model):
    """Event created by user"""

    __tablename__ = "user_event"

    user_event_id = db.Column(
        db.Integer, autoincrement=True, primary_key=True
    )
    event_id = db.Column(db.Integer, db.ForeignKey("events.event_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    attending = db.Column(db.Boolean)

    def __repr__(self):
        return (
            f"user_event_id ={self.user_event_id}\n"
            f"user_id = {self.user_id}\n"
            f"attending = {self.attending}"
        )


class Event(db.Model):
    """An event"""

    __tablename__ = "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    event_location_id = db.Column(
        db.Integer, db.ForeignKey("event_location.event_location_id"))
    event_type_id = db.Column(
        db.Integer, db.ForeignKey("event_types.event_type_id"))
    event_name = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    description = db.Column(db.Text)
    url_graphic = db.Column(db.String)

    def __repr__(self):
        return (
            f"event_id = {self.event_id}\n"
            f"user_id = {self.user_id}\n"
            f"event_location_id = {self.event_location_id}\n"
            f"event_type_id = {self.event_type}\n"
            f"event_name = {self.event_name}\n"
            f"start_date = {self.start_date}\n"
            f"end_date = {self.end_date}\n"
            f"start_time = {self.start_time}\n"
            f"end_time = {self.end_time}\n"
            f"description = {self.description}\n"
            f"url_graphic = {self.url_graphic}"
        )


class Event_Location(db.Model):
    """Event location longitude and latitude coordinates"""

    __tablename__ = "event_location"

    event_location_id = db.Column(
        db.Integer, autoincrement=True, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    def __repr__(self):
        return(
            f"event_location_id = {self.event_location_id}\n"
            f"longitude = {self.longitude}\n"
            f"latitude = {self.latitude}"
        )


class Event_Type(db.Model):
    """Returns type of event"""

    __tablename__ = "event_types"

    event_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_name = db.Column(db.String)

    def __repr__(self):
        return (
            f"event_type_id = {self.event_type_id}\n"
            f"type_name = {self.type_name}"
        )


"""Database Connection"""


def connect_to_db(flask_app,
                  db_uri="postgresql:///wild_bunch_database",
                  echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

    db.create_all()


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
