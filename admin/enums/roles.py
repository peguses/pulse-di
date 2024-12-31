from enum import Enum


class Roles(Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    GUEST = ("GUEST",)
    MARKETING_MANAGER = "MARKETING_MANAGER"
