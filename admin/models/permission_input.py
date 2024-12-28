from dataclasses import dataclass
from typing import List
from graphql import GraphQLError
from pydantic import BaseModel, field_validator
import strawberry

from admin.enums.actions import Actions


@dataclass
class PermissionBase:
    subject: str
    actions: List[Actions]


class PermissionInput(BaseModel, PermissionBase):

    @field_validator("actions")
    @classmethod
    def actions_must_be_valid(cls, value):
        if not value in Actions.__members__:
            action_list = ",".join([role.value for role in list(Actions)])
            raise GraphQLError(f"Actions should be on of {action_list}")


@strawberry.input
class PermissionInputRequest(PermissionBase):
    pass
