from typing import List
import strawberry

from admin.enums.actions import Actions


@strawberry.type
class PermissionType:
    subject: str
    actions: List[Actions]
