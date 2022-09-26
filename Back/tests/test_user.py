import pytest
import requests
from django import urls
import json
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@pytest.mark.django_db
def test_user_login():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'username': 'admin',
        'password': 'admin',
    }
    url = 'http://localhost:8000/login/'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 200
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_baduser_login():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'username': 'admi22',
        'password': 'admin',
    }
    url = 'http://localhost:8000/login/'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 404
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_user_badpswd_login():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'username': 'admin',
        'password': 'admi333n',
    }
    url = 'http://localhost:8000/login/'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 400
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_user_badpayload_login():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'username': 'admin',
        'pad': 'admin',
    }
    url = 'http://localhost:8000/login/'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 400
    assert response.headers['content-type'] == mimetype