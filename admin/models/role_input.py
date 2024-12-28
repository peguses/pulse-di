from dataclasses import dataclass
from typing import List
from graphql import GraphQLError
from pydantic import BaseModel, field_validator
import strawberry

from admin.models.permission_input import PermissionInput


@dataclass
class RoleBase:
    name: str
    role: str
    permissions: List[PermissionInput]


class ValidatableRoleInput(BaseModel, RoleBase):

    @field_validator("name")
    @classmethod
    def name_must_be_valid(cls, value):
        if not value.isalpha():
            raise GraphQLError("Role name should be string")
        return value


@strawberry.input
class RoleInputRequest(RoleBase):
    pass
