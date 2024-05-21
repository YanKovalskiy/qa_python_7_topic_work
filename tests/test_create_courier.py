import pytest
import allure


class TestCreateCourier:

    @allure.title('Создание курьера позитивный сценарий')
    def test_create_new_courier_positive_scenario(self, payload_to_create_courier, courier_endpoint):
        courier_endpoint.create_courier(payload_to_create_courier)
        courier_endpoint.check_status_code_is_(201)
        courier_endpoint.check_response_text_is_('{"ok":true}')

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_two_identical_courier(self, payload_to_create_courier, courier_endpoint):
        courier_endpoint.create_courier(payload_to_create_courier)
        courier_endpoint.create_courier(payload_to_create_courier)
        courier_endpoint.check_status_code_is_(409)
        courier_endpoint.check_response_message_is_('Этот логин уже используется. Попробуйте другой.')

    @allure.title('Создание курьера без заполнения одного из обязательных полей')
    @pytest.mark.parametrize(
        'required_field',
        ('login', 'password')
    )
    def test_create_courier_without_required_field(self, payload_to_create_courier, courier_endpoint, required_field):
        del payload_to_create_courier[required_field]
        courier_endpoint.create_courier(payload_to_create_courier)
        courier_endpoint.check_status_code_is_(400)
        courier_endpoint.check_response_message_is_('Недостаточно данных для создания учетной записи')

    @allure.title('Создание курьера без заполнения необязательных полей')
    def test_create_courier_without_first_name_field(self, payload_to_create_courier, courier_endpoint):
        del payload_to_create_courier['firstName']
        courier_endpoint.create_courier(payload_to_create_courier)
        courier_endpoint.check_status_code_is_(201)
        courier_endpoint.check_response_text_is_('{"ok":true}')
