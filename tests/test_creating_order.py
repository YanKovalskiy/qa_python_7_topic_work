import allure
import pytest


class TestOrder:

    @allure.title('Выбор цвета самоката в процессе оформления заказа')
    @pytest.mark.parametrize(
        'scooter_color',
        ([], ['BLACK'], ['GREY'], ['BLACK', 'GREY'])
    )
    def test_creating_order_with_choice_scooter_color(self, payload_to_order, order_endpoints, scooter_color):
        with allure.step(f'Выбираем цвет - {scooter_color}'):
            payload_to_order['color'] = scooter_color
        order_endpoints.create_order(payload_to_order)
        order_endpoints.check_status_code_is_(201)
        order_endpoints.check_in_response_is_field_('track')

    @allure.title('Получение списка заказов')
    def test_get_list_orders(self, order_endpoints):
        order_endpoints.get_list_orders()
        order_endpoints.check_status_code_is_(200)
        order_endpoints.check_in_response_is_field_('orders')
