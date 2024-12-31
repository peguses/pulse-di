# pylint: disable=C0116, C0103

from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI
from admin.exceptions.NotFoundException import NotFoundException
from admin.routers.auth_router import auth_router
from admin.routers.role_router import role_router
from admin.routers.user_router import user_router
from exceptions.exception_handler import (
    value_error_exception_handler,
    not_found_exception_handler,
)

app = FastAPI()

app.add_exception_handler(ValueError, value_error_exception_handler)
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(role_router, prefix="/roles", tags=["roles"])
app.include_router(user_router, prefix="/users", tags=["users"])
