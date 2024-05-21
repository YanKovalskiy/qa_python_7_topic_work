import allure


class Endpoint:
    response = None

    def check_status_code_is_(self, status_code):
        with allure.step(f'Проверяем код ответа. Код ответа - {self.response.status_code}'):
            assert self.response.status_code == status_code

    def check_response_text_is_(self, response_text):
        with allure.step('Проверяем текст ответа'):
            assert self.response.text == response_text

    def check_response_message_is_(self, response_text):
        with allure.step('Проверяем сообщение из ответа'):
            assert self.response.json()['message'] == response_text

    def check_in_response_text_is_text(self, text):
        with allure.step(f'Проверяем есть ли текст - {text} в ответе'):
            assert text in self.response.text
