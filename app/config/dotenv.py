from dotenv import load_dotenv
import os

load_dotenv()

# Get the environment variables
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")