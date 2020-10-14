from constants import EMAIL_PROMPT_TITLE
from pages.main_page import MainPage
from utils.string_util import has_numbers


class SighUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_email_edit_et')

        self.password_field = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_password_edit_et')
        self.sign_in_button = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_email_b')
        # password prompt elements
        self.password_prompt_title = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_password_requirements_title_tv')
        self.min_quantity_characters_check_mark = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_password_requirements_min_characters_iv')
        self.letters_check_mark = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_password_requirements_title_tv')
        self.numbers_checkmark = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_password_requirements_number_iv')
        self.special_character_checkmark = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_password_requirements_special_character_iv')
        self.progress_bar = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/sign_up_password_stregth_progress_pb')
        self.progress_bar_title = self.driver.instance.find_elements_by_id(
            'com.upside.consumer.android.beta:id/sign_up_password_stregth_text_tv')

    def _input_email(self, text):
        self.email_field.send_keys(text)

    def _input_password(self, text):
        self.password_field.send_keys(text)

    def fill_email_and_password(self, email, password):
        self._input_email(email)
        self._input_password(password)

    def _verify_email_prompt(self, email):
        if len(email) > 4:
            assert self.driver.instance.find_element_by_id(
                'com.upside.consumer.android.beta:id/sign_up_email_message_tv').text == EMAIL_PROMPT_TITLE
        # condition when there is no prompt (no element)

    def _verify_password_prompt(self, password):
        # conditionals for checking password prompt
        if has_numbers(password):
            assert self.numbers_checkmark.get_attribute("enabled")
        # add more checks

    def verify_promts(self, email, password):
        self._verify_email_prompt(email)
        self._verify_password_prompt(password)

    def click_sigh_in_button(self):
        self.sign_in_button.click()
        return MainPage()
