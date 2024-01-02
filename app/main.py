from fastapi import FastAPI

from .controllers.auth import router as auth_router
from .controllers.user_controller import router as user_router

from .middlewares.cors import setup_cors
from .middlewares.error_handling import add_exception_handlers


app = FastAPI(
    title="My App",
    description="My app description",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "user",
            "description": "Operations related to the User.",
        },
        {
            "name": "auth",
            "description": "Operations related to the Authentication.",
        }
    ],
)

# Middlewares
setup_cors(app)
add_exception_handlers(app)

# routes
app.include_router(auth_router)
app.include_router(user_router)


@app.get("/")
async def root():
    return {"msg": "Hello World"}



