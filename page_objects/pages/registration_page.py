from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class registration_page(object):
    def __init__(self, driver):
        self.driver = driver

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
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_field)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_field)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(last_name)

    def enter_email(self, email):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_field)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_field)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(password)

    def click_create_account(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_account_button)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.check_profile_title)
        ).text

    def get_error_message(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.error_msg)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.text