from dataclasses import dataclass
import re
from graphql import GraphQLError
from pydantic import BaseModel, field_validator
import strawberry

from admin.models.role_input import RoleInputRequest, ValidatableRoleInput

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
PASSWORD_REGEX = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"


@dataclass
class UserBase:
    firstName: str
    lastName: str
    email: str
    password: str
    role: RoleInputRequest


class UserInput(BaseModel, UserBase):
    email: str
    role: ValidatableRoleInput

    @field_validator("firstName")
    @classmethod
    def fist_name_must_be_valid(cls, value):
        if len(value) < 3:
            raise GraphQLError("First name must be at least 3 characters long")
        if not value.isalpha():
            raise GraphQLError("First name should only contain character")
        return value

    @field_validator("lastName")
    @classmethod
    def last_name_must_be_valid(cls, value):
        if len(value) < 3:
            raise GraphQLError("Last name must be at least 3 characters long")
        if not value.isalpha():
            raise GraphQLError("Last name should only contain character")
        return value

    @field_validator("email")
    @classmethod
    def email_must_be_valid(cls, value):
        if not re.match(EMAIL_REGEX, value):
            raise GraphQLError(f"Email {value} is not valid")
        return value

    @field_validator("password")
    @classmethod
    def password_must_be_valid(cls, value):
        if not re.match(PASSWORD_REGEX, value):
            raise GraphQLError("password not valid")
        return value


@strawberry.input
class UserInputRequest(UserBase):
    pass
