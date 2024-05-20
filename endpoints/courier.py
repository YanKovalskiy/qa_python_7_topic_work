import requests

from endpoints.base_endpoint import Endpoint
from config import URL


class Courier(Endpoint):

    def create_courier(self, payload):
        self.response = requests.post(f'{URL}/api/v1/courier', data=payload)
