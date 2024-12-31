from fastapi import Request
from fastapi.responses import JSONResponse
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
