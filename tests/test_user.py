from fastapi.testclient import TestClient
from app.main import app
from fastapi import status
from app.config.database import collection
from app.repositories.user_repository import find
from .utils.user_helper import get_user_id, clear_db
from time import sleep
client = TestClient(app)

clear_db()

def test_create_user():
    response = client.post(
        "/user",
        json = {
            "username": "test1",
            "email": "test1@gmail.com",
            "password": "123"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED

def test_create_user_with_existing_email():
    response = client.post(
        "/user",
        json = {
            "username": "test2",
            "email": "test1@gmail.com",
            "password": "1234"
        }
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_authenticate_user():
    response = client.post(
        "/auth",
        json = {
            "email": "test1@gmail.com",
            "password": "123"
        }
    )
    assert response.status_code == status.HTTP_302_FOUND

def test_authenticate_user_wrong_credentials():
    response = client.post(
        "/auth",
        json = {
            "email": "wrongEmail@gmail.com",
            "password":"wrongPassword"
        })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_get_user():
    user_id = get_user_id()
    print(user_id)
    response = client.get('/user/'+ user_id)
    assert response.status_code == status.HTTP_200_OK

def test_get_user_wrong_user_id():
    response = client.get('/user/wrong_user_id')
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_get_all_users():
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK

