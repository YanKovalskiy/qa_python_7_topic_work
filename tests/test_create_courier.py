import pytest
import allure

from endpoints.courier import Courier


class TestCreateCourier:

    @allure.title('Создание курьера позитивный сценарий')
    def test_create_new_courier_positive_scenario(self, payload):
        courier_endpoint = Courier()
        courier_endpoint.create_courier(payload)
        courier_endpoint.check_status_code_is_(201)
        courier_endpoint.check_response_text_is_('{"ok":true}')

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_two_identical_courier(self, payload):
        courier_endpoint = Courier()
        courier_endpoint.create_courier(payload)
        courier_endpoint.create_courier(payload)
        courier_endpoint.check_status_code_is_(409)
        courier_endpoint.check_response_message_is_('Этот логин уже используется')

    @allure.title('Создание курьера без заполнения одного из обязательных полей')
    @pytest.mark.parametrize(
        'required_field',
        ('login', 'password')
    )
    def test_create_courier_without_required_field(self, payload, required_field):
        del payload[required_field]
        courier_endpoint = Courier()
        courier_endpoint.create_courier(payload)
        courier_endpoint.check_status_code_is_(400)
        courier_endpoint.check_response_message_is_('Недостаточно данных для создания учетной записи')

    @allure.title('Создание курьера без заполнения необязательных полей')
    def test_create_courier_without_first_name_field(self, payload):
        del payload['firstName']
        courier_endpoint = Courier()
        courier_endpoint.create_courier(payload)
        courier_endpoint.check_status_code_is_(201)
        courier_endpoint.check_response_text_is_('{"ok":true}')
