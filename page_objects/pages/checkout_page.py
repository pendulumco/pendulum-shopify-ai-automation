from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.base_helper import BaseHelper

class CheckoutPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.baseHelper = BaseHelper(driver)

    email_input = (By.NAME, "email")
    country_dropdown = (By.ID, "Select0")
    canadian_alert = (By.XPATH, '//div[@role="alert"]')
    card_number_field = (By.CSS_SELECTOR, '[id="number"]')
    card_expiry_date_field = (By.NAME, "expiry")
    card_security_code_field = (By.CSS_SELECTOR, '[data-current-field="verification_value"]')
    pay_now_button = (By.ID, 'checkout-pay-button')
    first_name_field = (By.CSS_SELECTOR, '[name="firstName"]')
    last_name_field = (By.CSS_SELECTOR, '[name="lastName"]')
    address_field = (By.CSS_SELECTOR, '[name="address1"]')
    address_select_options = (By.CSS_SELECTOR, '[aria-label="Rancho Cucamonga High School, Lark Drive, Rancho '
                                               'Cucamonga, CA, USA"]')
    discount_code_field = (By.CSS_SELECTOR, '[name="reductions"]')
    apply_button = (By.CSS_SELECTOR, '[aria-label="Apply Discount Code"]')
    consent_checkbox = (By.ID, 'consent-checkbox')
    city_field = (By.CSS_SELECTOR, '[name="city"]')
    state_field = '[name="zone"]'
    postal_code_field = (By.CSS_SELECTOR, '[name="postalCode"]')
    complete_order_button = (By.CSS_SELECTOR, 'button[id="checkout-pay-button"]')
    order_confirmation = (By.ID, 'main-header')

    def enter_email(self, email):
        self.baseHelper.send_keys_to_element(self.email_input, email)

    def click_country_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.country_dropdown)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def set_country(self, country):
        self.baseHelper.select_option_by_value('[name="countryCode"]', country)

    def get_canadian_alert(self):
        return self.baseHelper.get_element_text(self.canadian_alert)

    def is_canadian_alert_absent(self):
        return self.baseHelper.is_element_present(self.canadian_alert)

    def check_if_exist_canadian_alert(self):
        element = self.driver.find_elements(*self.canadian_alert)
        return element.text

    def enter_card_number(self, iframe_selector, card_number):
        self.baseHelper.interact_with_iframe_send_keys(
            iframe_selector, self.card_number_field, card_number
        )

    def enter_card_expiry_date(self, iframe_selector, expiry_date):
        self.baseHelper.interact_with_iframe_send_keys_slowly(
            iframe_selector, self.card_expiry_date_field, expiry_date, delay=0.2
        )

    def enter_card_security_code(self, iframe_selector, security_code):
        self.baseHelper.interact_with_iframe_send_keys(
            iframe_selector, self.card_security_code_field, security_code
        )

    def click_pay_now(self):
        self.baseHelper.click_element(self.pay_now_button)

    def enter_first_name(self, first_name):
        self.baseHelper.send_keys_to_element(self.first_name_field, first_name)

    def enter_last_name(self, last_name):
        self.baseHelper.send_keys_to_element(self.last_name_field, last_name)

    def enter_address(self, address):
        self.baseHelper.send_keys_to_element(self.address_field, address)

    def select_address_option(self):
        self.baseHelper.click_element(self.address_select_options)

    def enter_discount_code(self, discount_code):
        self.baseHelper.send_keys_to_element(self.discount_code_field, discount_code)

    def click_apply_discount(self):
        self.baseHelper.click_element(self.apply_button)

    def check_consent_checkbox(self):
        self.baseHelper.click_element_javascript(self.consent_checkbox)

    def enter_city(self, city):
        self.baseHelper.send_keys_to_element(self.city_field, city)

    def enter_postal_code(self, postal_code):
        self.baseHelper.send_keys_to_element(self.postal_code_field, postal_code)

    def click_complete_order(self):
        self.baseHelper.click_element(self.complete_order_button)

    def select_state_by_value(self, value):
        self.baseHelper.select_option_by_value(self.state_field, value)

    def select_state_by_text(self, text):
        self.baseHelper.select_option_by_text(self.state_field, text)

    def get_order_confirmation(self):
        return self.baseHelper.get_element_text(self.order_confirmation)