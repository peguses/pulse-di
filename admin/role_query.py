from typing import List
import strawberry
from admin.models.role import RoleType
from admin.schemas.role import deserialize_roles
from config.database import role_collection


@strawberry.type
class RoleQuery:

    @strawberry.field
    async def get_roles(self) -> List[RoleType]:
        cursor = role_collection.find({})
        # async for role in cursor:
        #     return deserialize_role(role)
        roles = await cursor.to_list(length=10)
        print(roles)
        return deserialize_roles(roles)
