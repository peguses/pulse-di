from typing import List
import strawberry

from admin.models.permission_type import PermissionType


@strawberry.type
class RoleType:
    name: str
    role: str
    permissions: List[PermissionType]
