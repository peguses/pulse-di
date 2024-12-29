# pylint: disable=C0116, C0103

from fastapi import FastAPI
from admin.role_router import role_router
from admin.user_router import user_router
from exceptions.exception_handler import value_error_exception_handler

app = FastAPI()

app.add_exception_handler(ValueError, value_error_exception_handler)
app.include_router(role_router, prefix="/roles", tags=["roles"])
app.include_router(user_router, prefix="/users", tags=["users"])
