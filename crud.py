from model import db, User, connect_to_db


def create_user(first_name, last_name, email, phone, username,  password, user_location_id, user_event_id):
    """Create and return a new user"""

    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        username=username,
        password=password,
        user_location_id=user_location_id,
        user_event_id=user_event_id
    )

    return user


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
