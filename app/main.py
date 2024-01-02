from fastapi import FastAPI

from .controllers.auth import router as auth_router
from .controllers.user_controller import router as user_router

from .middlewares.cors import setup_cors
from .middlewares.error_handling import add_exception_handlers


app = FastAPI(
    title="API_REST FASTAPI MONGODB JWT LAYERED_ARCHITECTURE",
    description= """ 
    🚀 I'm thrilled to present our robust REST API powered by FastAPI, JWT authentication, and MongoDB, designed with a meticulous focus on a structured layered architecture! 🌐🛡️

🔐 Leveraging the exceptional capabilities of FastAPI, we meticulously crafted a secure and efficient system for user management. Our architecture, organized into distinct layers—models, services, controllers, and routes—ensures a clear separation of concerns, promoting code maintainability and scalability. 🏢🛠️

💻 By harnessing the power of JWT tokens, we established a strong foundation for authentication and authorization, guaranteeing secure user interactions throughout the application. 🗝️🔒

🐳 Our API is Dockerized using Docker Compose, streamlining deployment and scalability. This containerized approach not only simplifies deployment but also fosters a consistent environment across various platforms, maintaining our architecture's integrity. 🚀🐳

🧪 Furthermore, rigorous integration tests using FastAPI's TestClient were conducted, validating each layer's functionalities. Our commitment to a layered architecture ensures reliable and stable API operations. 🛠️🔍

📚 Explore our API's extensive documentation, highlighting endpoint details, parameters, and responses. Our layered architecture's clarity empowers developers to seamlessly integrate our services into their applications. 📖👨‍💻
""",
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



