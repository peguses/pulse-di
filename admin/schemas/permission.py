from typing import List

from admin.models.permission_input import PermissionInput
from admin.models.permission_type import PermissionType


def deserialize_permission(permission) -> PermissionType:
    return PermissionType(subject=permission["subject"], actions=permission["actions"])


def serialize_permission(permissions: List[PermissionInput]) -> dict:
    return [
        {"subject": permission.subject, "actions": permission.actions}
        for permission in permissions
    ]


def deserialize_permissions(permissions) -> List:
    return [serialize_permission(permission) for permission in permissions]
