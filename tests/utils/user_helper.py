from app.config.database import collection

def get_user_id():
    user =  collection.find_one({"email": "test1@gmail.com"})
    return str(user["_id"])

def clear_db():
    collection.delete_many({})