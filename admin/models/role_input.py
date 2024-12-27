import strawberry


@strawberry.input
class RoleInput:
    id: int
    name: str
    role: str
    # permissions: dict
