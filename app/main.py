from fastapi import FastAPI
# from app.routes.user_routes import router
from app.controllers.user_controller import router

app = FastAPI(
    title="My App",
    description="My app description",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "user",
            "description": "Operations related to the User.",
        },
    ],
)

#routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

