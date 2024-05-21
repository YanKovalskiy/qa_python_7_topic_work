import requests
import allure

from endpoints.base_endpoint import Endpoint
from config import URL


class OrderEndpoints(Endpoint):

    def create_order(self, payload):
        with allure.step(f'Отправляем запрос на создание заказа. payload={payload}'):
            self.response = requests.post(f'{URL}/api/v1/orders', json=payload)
