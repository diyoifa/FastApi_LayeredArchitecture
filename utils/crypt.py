from passlib.context import CryptContext
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encrypt_password(password:str):
    return crypt.hash(password)

def check_encrypted_password(password:str, hashed):
    return crypt.verify(password, hashed)