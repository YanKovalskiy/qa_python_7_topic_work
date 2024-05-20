import requests
import allure

from endpoints.base_endpoint import Endpoint
from config import URL


class Courier(Endpoint):

    def create_courier(self, payload):
        with allure.step('Отправляем запрос на создание курьера'):
            self.response = requests.post(f'{URL}/api/v1/courier', data=payload)
