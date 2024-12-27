import strawberry

from admin.enums.role import Role


@strawberry.type
class UserType:
    id: int
    firstName: str
    lastName: str
    email: str
    password: str
    role: Role
