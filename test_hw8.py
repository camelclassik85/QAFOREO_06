"""Документация API: https://restful-booker.herokuapp.com/apidoc/index.html

1. Воспроизвести все методы, рассмотренные на лекции - в файле test_api.py
2. С помощью метода PATCH внести некоторые изменения в ранее созданную запись бронирования
3. Проверить, что изменения применились"""

import requests
import pytest

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'


@pytest.fixture(scope='module')
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == 200
    assert 'token' in response_data
    yield token


@pytest.fixture(scope='module')
def booking_id():
    payload = {
        "firstname": "Jims",
        "lastname": "Browns",
        "totalprice": 1111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    assert response.status_code == 200
    yield booking_id


def test_partial_change_booking_info(auth_token, booking_id):
    payload = {
        "firstname": "Jims-updated",
        "lastname": "Browns-updated",
        "additionalneeds": "Lunch-updated"
    }
    headers = {'Cookie': f'token={auth_token}'}
    response = requests.patch(f'{BASE_URL}/{booking_id}', json=payload, headers=headers)
    assert response.status_code == 200
    response_get = requests.get(f'{BASE_URL}/{booking_id}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    print(response_data['firstname'])
    assert response_data['firstname'] == payload['firstname']
    print(response_data['lastname'])
    assert response_data['lastname'] == payload['lastname']
    print(response_data['additionalneeds'])
    assert response_data['additionalneeds'] == payload['additionalneeds']