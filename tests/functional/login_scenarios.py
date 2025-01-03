import time

import pytest
from page_objects.pages.home_page import HomePage
from constants import BASE_URL
from page_objects.pages.login import Login

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login_with_success(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page(BASE_URL)
        home_page.click_account_button()

        login = Login(driver)
        login.enter_email('raian.damaceno@pendulum.co')
        login.enter_password('teste')
        login.click_submit_login()
        time.sleep(5)

