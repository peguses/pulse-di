from typing import List
import strawberry

from admin.models.permission_input import PermissionInput


@strawberry.input
class RoleInput:
    name: str
    role: str
    permissions: List[PermissionInput]
