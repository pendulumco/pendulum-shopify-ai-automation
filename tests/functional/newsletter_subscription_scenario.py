import pytest
from page_objects.pages.home_page import HomePage
from constants import BASE_URL, SUCCESS_MESSAGE, ERROR_MESSAGE

@pytest.mark.usefixtures("driver")
class TestNewsletter:
    def test_valid_newsletter_registration(self, driver):
        newsletter = HomePage(driver)
        newsletter.open_home_page(BASE_URL)
        newsletter.enter_email("raian.damaceno@gmail.com")
        newsletter.click_submit_newsletter()

        success_message = newsletter.get_success_message()
        assert success_message == SUCCESS_MESSAGE, f"Expected '{SUCCESS_MESSAGE}', but got '{success_message}'"

    def test_invalid_newsletter_registration(self, driver):
        newsletter = HomePage(driver)
        newsletter.open_home_page(BASE_URL)
        newsletter.click_submit_newsletter()

        error_message = newsletter.get_error_message()
        assert error_message == ERROR_MESSAGE, f"Expected '{ERROR_MESSAGE}', but got '{error_message}'"
