from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# page_url = about:blank
class MetabolicDailyPage(object):
    def __init__(self, driver):
        self.driver = driver

    MD_3mo_radio_button = (By.CSS_SELECTOR, 'div[data-product="pendulum-metabolic-daily-membership-90-count"]')
    add_to_cart_button = (By.CSS_SELECTOR, 'button[type="submit"].btn.justify-content-center')
    upsell_modal_close = (By.CLASS_NAME, 'tingle-modal__close')

    def open_home_page(self, url):
        self.driver.get(url)

    def set_3months(self):
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MD_3mo_radio_button)
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

