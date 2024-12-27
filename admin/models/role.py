import strawberry


@strawberry.type
class Role:
    id: int
    name: str
    role: str
    # permissions: dict
