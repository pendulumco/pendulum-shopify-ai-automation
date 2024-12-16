from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# page_url = about:blank
class polyphenol_page(object):
    def __init__(self, driver):
        self.driver = driver

        def __init__(self, driver):
            self.driver = driver

    poly_1mo_radio_button = (By.CSS_SELECTOR, 'div[data-product="polyphenol-booster-membership"]')
    add_to_cart_button = (By.CSS_SELECTOR, 'button[type="submit"].btn.justify-content-center')
    upsell_modal_close = (By.CLASS_NAME, 'tingle-modal__close')

    def open_home_page(self, url):
        self.driver.get(url)

    def set_1month(self):
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.poly_1mo_radio_button)
        )
        radio_button.click()

    def click_add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

    def click_close_upsell_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.upsell_modal_close)
        ).click()
