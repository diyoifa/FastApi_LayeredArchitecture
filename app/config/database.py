from pymongo import MongoClient
from .dotenv import MONGO_DB_URI
try:
    client = MongoClient(MONGO_DB_URI)
    database = client.users_management
    collection = database.users
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")