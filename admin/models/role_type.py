import strawberry


@strawberry.type
class RoleType:
    name: str
    role: str
    # permissions: dict
