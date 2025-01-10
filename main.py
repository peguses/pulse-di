# pylint: disable=C0116, C0103

from graphql import GraphQLError
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI
from admin.exceptions.DuplicateEmailException import DuplicateEmailException
from admin.exceptions.NotFoundException import NotFoundException
from admin.routers.facebook_auth_router import facebook_auth_router
from admin.routers.googl_auth_router import google_auth_router
from routers.graphql_router import graphql_router
from fastapi.middleware.cors import CORSMiddleware

from exceptions.exception_handler import (
    duplicate_key_error_handler,
    value_error_exception_handler,
    not_found_exception_handler,
    graphql_error_handler,
)

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(ValueError, value_error_exception_handler)
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(GraphQLError, graphql_error_handler)
app.add_exception_handler(DuplicateEmailException, duplicate_key_error_handler)
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")
app.include_router(google_auth_router, prefix="/auth", tags=["auth"])
app.include_router(facebook_auth_router, prefix="/auth", tags=["auth"])
app.include_router(graphql_router, prefix="/graphql")
