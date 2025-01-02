from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import base_helper
from helpers.base_helper import BaseHelper


class registration_page:
    def __init__(self, driver):
        self.driver = driver
        self.baseHelper = BaseHelper(driver)

    first_name_field = (By.ID, 'customer-first-name')
    last_name_field = (By.ID, 'customer-last-name')
    email_field = (By.ID, 'customer-email')
    password_field = (By.ID, 'password')
    create_account_button = (By.XPATH, "//button[text()='Create Account']")
    check_profile_title = (By.CLASS_NAME, "text-center")
    error_msg = (By.CSS_SELECTOR, 'p.error-msg')

    def open_home_page(self, url):
        self.driver.get(url)

    def enter_first_name(self, first_name):
        self.baseHelper.send_keys_to_element(self.first_name_field, first_name)

    def enter_last_name(self, last_name):
        self.baseHelper.send_keys_to_element(self.last_name_field, last_name)

    def enter_email(self, email):
        self.baseHelper.send_keys_to_element(self.email_field, email)

    def enter_password(self, password):
        self.baseHelper.send_keys_to_element(self.password_field, password)

    def click_create_account(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_account_button)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def get_success_message(self):
        return self.baseHelper.get_element_text(self.check_profile_title)

    def get_error_message(self):
        return self.baseHelper.get_element_text(self.error_msg)