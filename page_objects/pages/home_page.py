from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    email_field = (By.CSS_SELECTOR, '#footer input.required.email')
    newsletter_submit_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn') and contains(@class, 'v4')]")
    error_msg = (By.CSS_SELECTOR, '#shopify-section-footer .error-msg')
    success_msg = (By.CSS_SELECTOR, '#shopify-section-footer .success-msg')
    close_modal_button = (By.CSS_SELECTOR, "button.modal-close")
    account_user = (By.CSS_SELECTOR, ".icon-user")
    shop_all_menu = (By.CLASS_NAME, "nav-1")
    GLP1_menu_options = (By.CSS_SELECTOR, 'a[href="/products/glp-1-probiotic"]')
    akk_menu_options = (By.CSS_SELECTOR, 'a[href="/products/pendulum-akkermansia"')
    md_menu_options = (By.CSS_SELECTOR, 'a[href="/products/pendulum-metabolic-daily-one-time"]')
    gc_menu_options = (By.CSS_SELECTOR, 'a[href="/products/pendulum-glucose-control-2-og"]')
    poly_menu_options = (By.CSS_SELECTOR, 'a[href="/products/polyphenol-booster-membership"]'
                                          '')
    # Methods
    def open_home_page(self, url):
        self.driver.get(url)

    def close_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_modal_button)
        ).click()


    def enter_email(self, email):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_field)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(email)

    def click_submit_newsletter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.newsletter_submit_button)
        ).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_msg)
        ).text

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_msg)
        ).text

    def click_account_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.account_user)
        ).click()

    def click_shop_all_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.shop_all_menu)
        ).click()

    def click_glp1_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.GLP1_menu_options)
        ).click()

    def click_Akkermansia_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.akk_menu_options)
        ).click()

    def click_md_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.md_menu_options)
        ).click()

    def click_gc_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.gc_menu_options)
        ).click()

    def click_poly_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.poly_menu_options)
        ).click()