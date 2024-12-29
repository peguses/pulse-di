from typing import List
from admin.models.role import RoleInputRequest, RoleType
from admin.schemas.permission import deserialize_permission, serialize_permission


def serialize_role(role: RoleInputRequest) -> dict:
    return {
        "name": role.name,
        "role": role.role.value,
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


def deserialize_roles(roles) -> List[RoleType]:
    return [deserialize_role(role) for role in roles]
