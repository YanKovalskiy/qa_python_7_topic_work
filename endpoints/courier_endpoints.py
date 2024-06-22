import requests
import allure

from endpoints.base_endpoint import Endpoint
from config import URL


class CourierEndpoints(Endpoint):

    def create_courier(self, payload):
        with allure.step(f'Отправляем запрос на создание курьера. payload={payload}'):
            self.response = requests.post(f'{URL}/api/v1/courier', data=payload)

    def login_courier(self, payload):
        with allure.step(f'Отправляем запрос на вход в систему. payload={payload}'):
            self.response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
            if self.response.status_code == 200:
                return self.response.json()['id']
            else:
                return None

    def delete_courier(self, id_courier):
        if id_courier is not None:
            with allure.step(f'Удаляем курьера с id = {id_courier}'):
                self.response = requests.delete(f'{URL}/api/v1/courier/{id_courier}')
