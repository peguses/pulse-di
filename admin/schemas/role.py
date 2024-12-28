from admin.models.role_input import RoleInputRequest
from admin.models.role_type import RoleType
from admin.schemas.permission import deserialize_permission, serialize_permission


def serialize_role(role: RoleInputRequest) -> dict:
    return {
        "name": role.name,
        "role": role.role,
        "permissions": serialize_permission(role.permissions),
    }


def deserialize_role(role) -> RoleType:
    return RoleType(
        name=role["name"],
        role=role["role"],
        permissions=[
            deserialize_permission(permission) for permission in role["permissions"]
        ],
    )
