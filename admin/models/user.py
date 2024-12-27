import strawberry


@strawberry.type
class User:
    id: int
    firstName: str
    lastName: str
    email: str
    password: str
    # role: Role
