from typing import List
from admin.models.user import User
from admin.models.user_input import UserInput


def deserialize_user(user) -> User:

    return User(
        id=user["_id"],
        firstName=user["firstName"],
        lastName=user["lastName"],
        email=user["email"],
        password=user["password"],
    )


def serialize_user(user: UserInput) -> dict:
    return {
        "firstName": str(user.firstName),
        "lastName": str(user.lastName),
        "email": str(user.email),
        "password": str(user.password),
        # "role": dict(serialize_role(user["role"])),
    }


def deserialize_users(users) -> List:
    return [serialize_user(user) for user in users]
