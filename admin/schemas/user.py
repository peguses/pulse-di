from typing import List
from admin.models.permission import PermissionInputRequest, PermissionInput
from admin.models.role import RoleInput
from admin.models.user import UserInput, UserInputRequest, UserType
from admin.schemas.role import deserialize_role, serialize_role


def deserialize_user(user) -> UserType:
    return UserType(
        id=user["_id"],
        first_name=user["first_name"],
        last_name=user["last_name"],
        email=user["email"],
        password=user["password"],
        role=deserialize_role(user["role"]),
    )


def deserialize_users(users) -> List:
    return [deserialize_user(user) for user in users]


def validate_and_serialize_user(user: UserInputRequest) -> dict:
    user_data = validate_user(user)
    return {
        "first_name": str(user_data.first_name),
        "last_name": str(user_data.last_name),
        "email": str(user_data.email),
        "password": str(user_data.password),
        "role": serialize_role(user_data.role),
    }


def validate_user(user: UserInputRequest) -> UserInputRequest:
    return UserInput(
        id=None,
        first_name=user.first_name,
        last_name=user.last_name,
        password=user.password,
        email=user.email,
        role=RoleInput(
            name=user.role.name,
            role=user.role.role,
            permissions=__build_permission_list(user.role.permissions),
        ),
    )


def __build_permission_list(
    permissions: List[PermissionInputRequest],
) -> List[PermissionInput]:
    return [
        PermissionInput(subject=permission.subject, actions=permission.actions)
        for permission in permissions
    ]
