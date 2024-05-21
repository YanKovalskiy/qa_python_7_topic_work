import requests
import allure

from endpoints.base_endpoint import Endpoint
from config import URL


class OrderEndpoints(Endpoint):

    def create_order(self, payload):
        with allure.step(f'Отправляем запрос на создание заказа. payload={payload}'):
            self.response = requests.post(f'{URL}/api/v1/orders', json=payload)

    def get_list_orders(self):
        with allure.step(f'Отправляем запрос на получение списка заказов'):
            self.response = requests.get(f'{URL}/api/v1/orders')
