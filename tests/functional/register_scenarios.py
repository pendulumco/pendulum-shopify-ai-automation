import pytest
import random
from page_objects.pages.home_page import HomePage
from constants import REGISTER_URL, SUCCESS_MESSAGE, ERROR_MESSAGE
from page_objects.pages.registration_page import registration_page


@pytest.mark.usefixtures("driver")
class TestRegister:
    # @pytest.skip
    # def test_successful_registration(self, driver):
    #     register = registration_page(driver)
    #     register.open_home_page(REGISTER_URL)
    #
    #     random_number = random.randint(1, 10000)
    #     email_value = f'automation_tests_{random_number}@tests.com'
    #
    #     register.enter_first_name('Test')
    #     register.enter_last_name('Automation')
    #     register.enter_email(email_value)
    #     register.enter_password('teste')
    #     register.click_create_account()
    #
    #     result = register.get_success_message()
    #     assert result == f"Welcome, Test"

    def test_registration_missing_password(self, driver):
        register = registration_page(driver)
        register.open_home_page(REGISTER_URL)

        random_number = random.randint(1, 10000)
        email_value = f'automation_tests_{random_number}@tests.com'

        register.enter_first_name('Test')
        register.enter_last_name('Automation')
        register.enter_email(email_value)
        register.click_create_account()

        result = register.get_error_message()
        assert result == f"Please complete all the required fields."

    def test_registration_missing_email(self, driver):
        register = registration_page(driver)
        register.open_home_page(REGISTER_URL)

        random_number = random.randint(1, 10000)
        email_value = f'automation_tests_{random_number}@tests.com'

        register.enter_first_name('Test')
        register.enter_last_name('Automation')
        register.enter_password('teste')
        register.click_create_account()

        result = register.get_error_message()
        assert result == f"Please complete all the required fields."

    def test_registration_missing_first_name(self, driver):
        register = registration_page(driver)
        register.open_home_page(REGISTER_URL)

        random_number = random.randint(1, 10000)
        email_value = f'automation_tests_{random_number}@tests.com'

        register.enter_last_name('Automation')
        register.enter_email(email_value)
        register.enter_password('teste')
        register.click_create_account()

        result = register.get_error_message()
        print(result)
        assert result == f"Please complete all the required fields."

    def test_registration_missing_last_name(self, driver):
        register = registration_page(driver)
        register.open_home_page(REGISTER_URL)

        random_number = random.randint(1, 10000)
        email_value = f'automation_tests_{random_number}@tests.com'

        register.enter_first_name('Test')
        register.enter_email(email_value)
        register.enter_password('teste')
        register.click_create_account()

        result = register.get_error_message()
        assert result == f"Please complete all the required fields."
