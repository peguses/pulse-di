from typing import List
from admin.models.permission_input import PermissionInput
from admin.models.role_input import RoleInput
from admin.models.user_type import UserType
from admin.models.user_input import UserInput, UserInputRequest
from admin.schemas.role import deserialize_role, serialize_role


def deserialize_user(user) -> UserType:
    return UserType(
        id=user["_id"],
        firstName=user["firstName"],
        lastName=user["lastName"],
        email=user["email"],
        password=user["password"],
        role=deserialize_role(user["role"]),
    )


def deserialize_users(users) -> List:
    return [deserialize_user(user) for user in users]


def validate_and_serialize_user(user: UserInputRequest) -> dict:
    user_data = validate_user(user)
    return {
        "firstName": str(user_data.firstName),
        "lastName": str(user_data.lastName),
        "email": str(user_data.email),
        "password": str(user_data.password),
        "role": serialize_role(user_data.role),
    }


def validate_user(user: UserInputRequest) -> UserInputRequest:
    print(user)
    return UserInput(
        firstName=user.firstName,
        lastName=user.lastName,
        password=user.password,
        email=user.email,
        role=RoleInput(
            name=user.role.name,
            role=user.role.role,
            # permissions=PermissionInput(subject=user.role.permissions),
        ),
    )
