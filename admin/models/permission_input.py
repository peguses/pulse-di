from typing import List
import strawberry

from admin.enums.actions import Actions


@strawberry.input
class PermissionInput:
    subject: str
    actions: List[Actions]
