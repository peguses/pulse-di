import strawberry


@strawberry.input
class UserInput:
    firstName: str
    lastName: str
    email: str
    password: str
    # role: RoleInput
