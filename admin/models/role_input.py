import strawberry


@strawberry.input
class RoleInput:
    name: str
    role: str
    permissions: dict
