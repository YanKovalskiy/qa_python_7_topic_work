import pytest
import random

import helpers

from faker import Faker
from datetime import datetime, timedelta

from endpoints.courier_endpoints import CourierEndpoints
from endpoints.order_endpoints import OrderEndpoints


@pytest.fixture()
def courier_endpoints():
    return CourierEndpoints()


@pytest.fixture()
def order_endpoints():
    return OrderEndpoints()


@pytest.fixture()
def payload_to_create_courier():
    payload = helpers.generate_payload()
    payload_to_delete = {key: value for key, value in payload.items()}
    del payload_to_delete['firstName']

    yield payload

    helpers.delete_courier_data(payload_to_delete)


@pytest.fixture()
def payload_to_login(courier_endpoints):
    payload = helpers.generate_payload()
    courier_endpoints.create_courier(payload)
    del payload['firstName']

    yield payload

    helpers.delete_courier_data(payload)


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
        "deliveryDate": str(datetime.now() + timedelta(days=1))[:10],
        "comment": "Комментарий курьеру",
        "color": []
    }
    return payload
