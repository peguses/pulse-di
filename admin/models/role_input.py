from dataclasses import dataclass
from typing import List, Optional
from graphql import GraphQLError
from pydantic import BaseModel, field_validator
import strawberry

from admin.enums.roles import Roles
from admin.models.permission_input import PermissionInput, PermissionInputRequest


@dataclass
class RoleBase:
    name: str
    role: str
    permissions: Optional[List[PermissionInputRequest]]


class RoleInput(BaseModel, RoleBase):

    permissions: PermissionInput

    @field_validator("name")
    @classmethod
    def name_must_be_valid(cls, value):
        if not value.isalpha():
            raise GraphQLError("Role name should be string")
        return value

    @field_validator("role")
    @classmethod
    def role_must_be_valid(cls, value):
        if not value in Roles.__members__:
            role_list = ",".join([role.value for role in list(Roles)])
            raise GraphQLError(f"Role should be on of {role_list}")


@strawberry.input
class RoleInputRequest(RoleBase):
    pass
