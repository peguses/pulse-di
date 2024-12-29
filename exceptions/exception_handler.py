from fastapi import Request
from fastapi.responses import JSONResponse


async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Bad Request",
            "message": str(exc),  # The error message from the ValueError
            "details": "The input value is not valid.",
        },
    )
