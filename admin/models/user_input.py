import strawberry

from admin.models.role_input import RoleInput


@strawberry.input
class UserInput:
    firstName: str
    lastName: str
    email: str
    password: str
    role: RoleInput
