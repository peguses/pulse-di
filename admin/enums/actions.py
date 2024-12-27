from enum import Enum


class Actions(str, Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    VIEW = "VIEW"
    DELETE = "DELETE"
    MANAGE = "MANAGE"
