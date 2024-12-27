from admin.models.role_input import RoleInput
from admin.models.role_type import RoleType


def serialize_role(role: RoleInput) -> dict:

    return {
        "name": role.name,
        "role": role.role,
        # "permissions": List(serialize_permissions(role["permissions"])),
    }


def deserialize_role(role) -> RoleType:
    return RoleType(name=role["name"], role=role["role"])
