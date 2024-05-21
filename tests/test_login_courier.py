import pytest
import allure


class TestLoginCourier:
    @allure.title('Вход в систему зарегистрированного курьера позитивный сценарий')
    def test_login_courier_positive_scenario(self, payload_to_login, courier_endpoint):
        courier_endpoint.login_courier(payload_to_login)
        courier_endpoint.check_status_code_is_(200)
        courier_endpoint.check_in_response_text_is_text('id')

    @allure.title('Вход в систему зарегистрированного курьера без заполнения одного из обязательных полей')
    @pytest.mark.parametrize(
        'required_field',
        ('login', 'password')
    )
    def test_login_without_required_field(self, payload_to_login, courier_endpoint, required_field):
        del payload_to_login[required_field]
        courier_endpoint.login_courier(payload_to_login)
        courier_endpoint.check_status_code_is_(400)
        courier_endpoint.check_response_message_is_('Недостаточно данных для входа')

    @allure.title('Вход в систему с неправильно указанными логином или паролем')
    @pytest.mark.parametrize(
        'not_correct_field',
        ('login', 'password')
    )
    def test_login_with_not_correct_field(self, payload_to_login, courier_endpoint,  not_correct_field):
        payload_to_login[not_correct_field] = 'notcorrect'
        courier_endpoint.login_courier(payload_to_login)
        courier_endpoint.check_status_code_is_(404)
        courier_endpoint.check_response_message_is_('Учетная запись не найдена')
