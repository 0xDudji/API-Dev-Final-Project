import requests
import json

def test_get_users():
    response = requests.get('http://127.0.0.1:8000/users/')
    assert response.status_code == 200

def test_get_user_id():
    response = requests.get('http://127.0.0.1:8000/users/1')
    assert response.status_code == 200

def test_get_reviews():
    response = requests.get('http://127.0.0.1:8000/reviews')
    assert response.status_code == 200

def test_get_no_user():
    response = requests.get('http://127.0.0.1:8000/users/1000')
    assert response.status_code == 404

    