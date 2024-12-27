import strawberry


@strawberry.type
class RoleType:
    id: int
    name: str
    role: str
    permissions: dict
