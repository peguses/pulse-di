import strawberry

from admin.models.role_type import RoleType


@strawberry.type
class UserType:
    id: int
    firstName: str
    lastName: str
    email: str
    password: str
    role: RoleType
