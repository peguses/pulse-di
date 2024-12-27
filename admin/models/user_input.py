import strawberry

from admin.enums.role import Role


@strawberry.input
class UserInput:
    firstName: str
    lastName: str
    email: str
    password: str
    role: Role
