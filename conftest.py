import pytest
import random
import string

from faker import Faker

from endpoints.courier_endpoints import CourierEndpoints
from endpoints.order_endpoints import OrderEndpoints


def generate_payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


@pytest.fixture()
def courier_endpoints():
    return CourierEndpoints()


@pytest.fixture()
def order_endpoints():
    return  OrderEndpoints()


def delete_courier_data(payload):
    courier_endpoint = CourierEndpoints()
    id_courier = courier_endpoint.login_courier(payload)
    courier_endpoint.delete_courier(id_courier)


@pytest.fixture()
def payload_to_create_courier():
    payload = generate_payload()
    payload_to_delete = {key: value for key, value in payload.items()}
    del payload_to_delete['firstName']

    yield payload

    delete_courier_data(payload_to_delete)


@pytest.fixture()
def payload_to_login(courier_endpoints):
    payload = generate_payload()
    courier_endpoints.create_courier(payload)
    del payload['firstName']

    yield payload

    delete_courier_data(payload)


@pytest.fixture()
def payload_to_order():
    fake = Faker(locale='ru_RU')
    gender = random.choice(('male', 'female'))
    payload = {
        "firstName": (fake.first_name_female() if gender == 'female' else fake.first_name_male()),
        "lastName":  (fake.last_name_female() if gender == 'female' else fake.last_name_male()),
        "address": fake.address(),
        "metroStation": 4,
        "phone": fake.phone_number(),
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Комментарий курьеру",
        "color": []
    }
    return payload
