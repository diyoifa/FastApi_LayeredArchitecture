from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi import status
from fastapi.exceptions import RequestValidationError, HTTPException
from jose import JWTError
from pymongo.errors import PyMongoError

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

async def request_validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": exc.errors()},
    )

async def jwt_exception_handler(request: Request, exc: JWTError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"message": "Could not validate credentials"},
    )

async def mongo_exception_handler(request: Request, exc: PyMongoError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Database error"},
    )

def add_exception_handlers(app: FastAPI):
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    app.add_exception_handler(JWTError, jwt_exception_handler)
    app.add_exception_handler(PyMongoError, mongo_exception_handler)
