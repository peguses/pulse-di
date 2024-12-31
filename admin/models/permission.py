from dataclasses import dataclass
from typing import List
from pydantic import BaseModel, field_validator
import strawberry

from admin.enums.actions import Actions


@dataclass
class PermissionBase:
    subject: str
    actions: List[Actions]


class PermissionInput(BaseModel, PermissionBase):

    @field_validator("subject")
    @classmethod
    def actions_must_be_valid(cls, value):
        # if not any(value in values for value in Actions.__members__):
        #     action_list = ",".join([role.value for role in Actions])
        #     raise GraphQLError(f"Actions should be on of {action_list}")
        return value


@strawberry.input
class PermissionInputRequest(PermissionBase):
    actions: List[Actions]


@strawberry.type
class PermissionType(PermissionBase):
    actions: List[Actions]
