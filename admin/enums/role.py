from enum import Enum


class Role(str, Enum):
    ADMIN = "ADMIN"
    GUEST = "GUEST"
    CAMPAIGN_ADMIN = "CAMPAIGN_ADMIN"
    MANAGER = "MANAGER"
