import os
from pymongo import MongoClient

try:
    client = MongoClient(
        'mongodb+srv://test1002542235:Cielo151.@cluster0.70zx4ii.mongodb.net/'
    )
    database = client.users_management
    collection = database.users
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")