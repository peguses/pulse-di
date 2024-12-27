from typing import List
from admin.schemas.permission import serialize_permissions


def serialize_role(role) -> dict:
    return {
        "id": str(role["id"]),
        "name": str(role["name"]),
        "role": str(role["role"]),
        "permissions": List(serialize_permissions(role["permissions"])),
    }
