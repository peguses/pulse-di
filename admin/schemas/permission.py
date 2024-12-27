from typing import List


def serialize_permission(permission) -> dict:
    return {
        "subject": str(permission["subject"]),
        "actions": List(permission["actions"]),
    }


def serialize_permissions(permissions) -> List:
    return [serialize_permission(permission) for permission in permissions]
