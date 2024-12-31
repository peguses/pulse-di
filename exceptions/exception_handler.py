from fastapi import Request
from fastapi.responses import JSONResponse
from graphql import GraphQLError
from admin.exceptions.DuplicateEmailException import DuplicateEmailException
from admin.exceptions.NotFoundException import NotFoundException


async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Bad Request",
            "message": str(exc),  # The error message from the ValueError
            "details": "The input value is not valid.",
        },
    )


async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404, content={"error": "Not found", "message": str(exc)}
    )


async def graphql_error_handler(request: Request, exc: GraphQLError):
    return JSONResponse(
        status_code=400, content={"error": "Bad Request", "message": str(exc)}
    )


async def duplicate_key_error_handler(request: Request, exc: DuplicateEmailException):
    return JSONResponse(
        status_code=409, content={"error": "Duplicate Key", "message": str(exc)}
    )
