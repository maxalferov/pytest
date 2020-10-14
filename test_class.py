import pytest

from driver import Driver
from pages.login_page import LoginPage


class TestClass:

    def setup(self):
        # init_something()
        print("Creating driver")
        self.driver = Driver()
        self.driver.instance.implicitly_wait(10)

    def teardown(self):
        self.driver.instance.quit()
        print("TearDown")

    def _click_allow(self):
        self.driver.instance.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()

    # 3 item Write automated tests for Sign up with email feature.
    @pytest.mark.parametrize("test_input_email, test_input_password",
                             [("EMAIL1", "Password1"), ("EMAIL2", "Password2"), ("EMAIL3", "Password3")])
    def test_sign_up_with_valid_credentials(self, test_input_email, test_input_password):
        print('Sigh Up with valid credentials')
        self._click_allow()
        login = LoginPage(self.driver)
        sigh_up_page = login.tap_to_sigh_up_button()
        sigh_up_page.fill_email_and_password(test_input_email, test_input_password)
        sigh_up_page.verify_promts(test_input_email, test_input_password)
        sigh_up_page.click_sigh_in_button()

        assert 1 == 1

    @pytest.mark.parametrize("test_input_email, test_input_password",
                             [("11111", "Password1"), ("EMAIL2", ""), ("", "")])
    def test_sign_up_with_invalid_credentials(self, test_input_email, test_input_password):
        print('Sigh Up with invalid credentials')
        self._click_allow()
        login = LoginPage(self.driver)
        sigh_up_page = login.tap_to_sigh_up_button()
        sigh_up_page.fill_email_and_password(test_input_email, test_input_password)
        sigh_up_page.verify_promts(test_input_email, test_input_password)
        sigh_up_page.click_sigh_in_button()

        assert 1 == 2

# 1 item - tests for sigh in, sigh up
