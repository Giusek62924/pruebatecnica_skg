import pytest
import requests
from django import urls
import json
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@pytest.mark.django_db
def test_getwithoutauth_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    url = 'http://localhost:8000/api/master/'
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 401
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_getwithauth_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }

    url = 'http://localhost:8000/api/master/'
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_getwithauth_data_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }

    url = 'http://localhost:8000/api/master/'
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    assert response.json()
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_getonewithoutauth_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    url = 'http://localhost:8000/api/master/5/'
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 401
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_getonewithauth_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }

    url = 'http://localhost:8000/api/master/5/'
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_getonewithauth_data_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }

    url = 'http://localhost:8000/api/master/5/'
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    assert response.json()
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_getonewithauth_404_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }

    url = 'http://localhost:8000/api/master/100000/'
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 404
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_createdata_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }
    data = {
        'entity': 1,
        'city': 1,
        'role' : 1
    }
    url = 'http://localhost:8000/api/master/'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 201
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_createdata_withoutauth_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }
    data = {
        'entity': 1,
        'city': 1,
        'role' : 1
    }
    url = 'http://localhost:8000/api/master/'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 401
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_createdata_withbaddata_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }
    data = {
        'entity': 100,
        'city': 1,
        'role' : 1
    }
    url = 'http://localhost:8000/api/master/'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 400
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_createdata_withoutdata_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }
    data = {
        'entity': 100,

    }
    url = 'http://localhost:8000/api/master/'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 400
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_delete_withoutdata_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }

    url = 'http://localhost:8000/api/master/2/'
    response = requests.delete(url, headers=headers)
    
    assert response.status_code == 404
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_delete_withoutdataandtoken_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }

    url = 'http://localhost:8000/api/master/2/'
    response = requests.delete(url, headers=headers)
    
    assert response.status_code == 401
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_Putdata_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }
    data = {
        'entity': 1,
        'city': 1,
        'role' :1

    }
    url = 'http://localhost:8000/api/master/5/'
    response = requests.put(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 200
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_Putdata_data_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
        'Authorization' : "Token 088f818cf92a322fa36bd14cab4b9fa1c0093616"
    }
    data = {
        'entity': 1,
        'city': 1,
        'role' :1

    }
    url = 'http://localhost:8000/api/master/5/'
    response = requests.put(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 200
    assert response.json()
    assert response.headers['content-type'] == mimetype

@pytest.mark.django_db
def test_Putdata_withoutoken_master():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }
    data = {
        'entity': 1,
        'city': 1,
        'role' :1

    }
    url = 'http://localhost:8000/api/master/5/'
    response = requests.put(url, data=json.dumps(data), headers=headers)
    
    assert response.status_code == 401
    assert response.headers['content-type'] == mimetype