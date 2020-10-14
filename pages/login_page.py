from pages.sigh_up_page import SighUpPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.apple_button = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/login_sign_in_with_apple_b')
        self.google_button = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/login_sing_in_google_b')
        self.fb_button = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/login_sing_in_fb_b')
        self.sign_up_button = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/login_sing_up_email_b')
        self.login_button = self.driver.instance.find_element_by_id(
            'com.upside.consumer.android.beta:id/login_clickable_tv')

    def tap_to_apple_button(self):
        print('Click on Apple Button')
        self.apple_button.click()

    def tap_to_sigh_up_button(self):
        print('Click on Sigh Up button')
        self.sign_up_button.click()
        return SighUpPage(self.driver)
