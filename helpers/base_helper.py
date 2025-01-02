import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseHelper:
    def __init__(self, driver):
        self.driver = driver

    def interact_with_iframe_send_keys(self, iframe_selector, element_selector, text):
        try:
            iframe = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, iframe_selector))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
            self.driver.switch_to.frame(iframe)

            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(element_selector)
            )
            element.clear()
            element.send_keys(text)
        finally:
            self.driver.switch_to.default_content()

    def interact_with_iframe_send_keys(self, iframe_selector, element_selector, text):
        try:
            iframe = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, iframe_selector))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
            self.driver.switch_to.frame(iframe)

            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(element_selector)
            )
            element.clear()
            element.send_keys(text)
        finally:
            self.driver.switch_to.default_content()

    def interact_with_iframe_send_keys_slowly(self, iframe_selector, element_selector, text, delay=0.1):
        try:
            iframe = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, iframe_selector))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
            self.driver.switch_to.frame(iframe)

            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(element_selector)
            )
            element.clear()

            for char in text:
                element.send_keys(char)
                time.sleep(delay)
        finally:
            self.driver.switch_to.default_content()

    def select_option_by_value(self, select_selector, value):
        select_element = self.driver.find_element(By.CSS_SELECTOR, select_selector)
        select = Select(select_element)
        select.select_by_value(value)

    def select_option_by_text(self, select_selector, text):
        select_element = self.driver.find_element(By.CSS_SELECTOR, select_selector)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def click_element(self, selector, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(selector)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def send_keys_to_element(self, selector, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(selector)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, selector, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(selector)
        )
        return element.text

    def is_element_present(self, selector, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(selector)
            )
            return True
        except TimeoutException:
            return False
