class Endpoint:
    response = None

    def check_status_code_is_(self, status_code):
        assert self.response.status_code == status_code

    def check_response_text_is_(self, response_text):
        assert self.response.text == response_text

    def check_response_message_is_(self, response_text):
        assert self.response.json()['message'] == response_text
