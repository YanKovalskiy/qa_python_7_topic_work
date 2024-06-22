import string
import random

from endpoints.courier_endpoints import CourierEndpoints


def generate_payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
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


def delete_courier_data(payload):
    courier_endpoint = CourierEndpoints()
    id_courier = courier_endpoint.login_courier(payload)
    courier_endpoint.delete_courier(id_courier)
