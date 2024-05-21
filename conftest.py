import pytest
import random
import string

from endpoints.courier_endpoints import CourierEndpoints


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
def courier_endpoint():
    return CourierEndpoints()


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
def payload_to_login(courier_endpoint):
    payload = generate_payload()
    courier_endpoint.create_courier(payload)
    del payload['firstName']

    yield payload

    delete_courier_data(payload)
