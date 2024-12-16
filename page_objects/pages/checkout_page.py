from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# page_url = about:blank
class CheckoutPage(object):
    def __init__(self, driver):
        self.driver = driver

    email_input = (By.NAME, "email")
    country_dropdown = (By.ID, "Select0")
    canadian_alert = (By.XPATH, '//div[@role="alert"]')
    card_number_field = (By.ID, 'number')
    card_expiry_date_field = (By.ID, 'expiry')
    card_security_code_field = (By.ID, 'verification_value')
    pay_now_button = (By.ID, 'checkout-pay-button')
    first_name_field = (By.ID, 'TextField0')
    last_name_field = (By.ID, 'TextField1')
    address_field = (By.ID, 'shipping-address1')
    address_select_options = (By.CSS_SELECTOR, '[aria-label="Rancho Cucamonga High School, Lark Drive, Rancho '
                                               'Cucamonga, CA, USA"]')
    discount_code_field = (By.ID, 'ReductionsInput5')
    apply_button = (By.CSS_SELECTOR, '[aria-label="Apply Discount Code"]')
    consent_checkbox = (By.ID, 'consent-checkbox')

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.email_input)
        ).send_keys(email)

    def click_country_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.country_dropdown)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def set_country(self, country):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//option[@value="{country}"]'))
        ).click()

    def get_canadian_alert(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.canadian_alert)
        )
        return element.text

    def is_canadian_alert_absent(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.canadian_alert)
            )
            return False
        except TimeoutException:
            return True

    def check_if_exist_canadian_alert(self):
        element = self.driver.find_elements(*self.canadian_alert)
        return element.text

    def enter_card_number(self, card_number):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_number_field)
        )
        element.clear()
        element.send_keys(card_number)

    def enter_card_expiry_date(self, expiry_date):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_expiry_date_field)
        )
        element.clear()
        element.send_keys(expiry_date)

    def enter_card_security_code(self, security_code):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_security_code_field)
        )
        element.clear()
        element.send_keys(security_code)

    def click_pay_now(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pay_now_button)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def enter_first_name(self, first_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_field)
        )
        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_field)
        )
        element.clear()
        element.send_keys(last_name)

    def enter_address(self, address):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.address_field)
        )
        element.clear()
        element.send_keys(address)

    def select_address_option(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.address_select_options)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def enter_discount_code(self, discount_code):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.discount_code_field)
        )
        element.clear()
        element.send_keys(discount_code)

    def click_apply_discount(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.apply_button)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def check_consent_checkbox(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.consent_checkbox)
        )
        self.driver.execute_script("arguments[0].click();", element)
