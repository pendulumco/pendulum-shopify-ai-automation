from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helpers.base_helper import BaseHelper
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.baseHelper = BaseHelper(driver)

    # Locators
    email_address_field = (By.NAME, 'customer[email]')
    password_field = (By.NAME, 'customer[password]')
    login_submit_button = (By.CSS_SELECTOR, "#customer_login [type='submit']")
    check_profile_title = (By.CLASS_NAME, "text-center")
    modal_shop_close = (By.CSS_SELECTOR, ".sda-modal-close-button")
    # Methods

    def enter_email(self, email):
        self.baseHelper.send_keys_to_element(self.email_address_field, email)

    def enter_password(self, password):
        self.baseHelper.send_keys_to_element(self.password_field, password)

    def click_submit_login(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_submit_button)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def click_close_modal(self):
        self.driver.find_element(*self.modal_shop_close).click()

    def get_success_message(self):
        return self.baseHelper.get_element_text(self.check_profile_title)
