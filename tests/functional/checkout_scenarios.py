import pytest
from page_objects.pages.cart import CartPage
from page_objects.pages.checkout_page import CheckoutPage
from page_objects.pages.home_page import HomePage
from constants import BASE_URL
from page_objects.pages.products_page import products_page


@pytest.mark.usefixtures("driver")
class TestCanadianScenarios:
    checkout_details = {
        'first_name': 'Adriana',
        'last_name': 'P Pugliesi',
        'address': 'Rancho Cucamonga High School Pool',
        'city': 'Rancho Cucamonga',
        'postal_code': '91701',
        'state': 'California',
        'card_number': '4859538758583507',
        'card_cvc': '206',
        'card_expiry': '9/26',
        'name_card': 'Raian S Damaceno'
    }

    def set_product_option(self, driver, data_product):
        product = products_page(driver)
        product.set_radio_data_product(data_product)
        product.click_add_to_cart()
        product.click_close_upsell_modal()

    def select_product(self, driver, product):
        home_page = HomePage(driver)
        home_page.open_home_page(BASE_URL)
        home_page.click_shop_all_menu()
        home_page.select_product(product)

    def set_cart_quantity(self, driver, quantity):
        cart = CartPage(driver)
        cart.set_item_qtd(quantity)
        cart.click_continue_to_checkout()

    def set_checkout_information(self, driver, checkout_details):
        checkout = CheckoutPage(driver)
        checkout.enter_email('raian.damaceno@pendulum.co')
        checkout.enter_first_name(checkout_details['first_name'])
        checkout.enter_last_name(checkout_details['last_name'])
        checkout.enter_address(checkout_details['address'])
        checkout.enter_city(checkout_details['city'])
        checkout.enter_postal_code(checkout_details['postal_code'])
        checkout.select_state_by_text(checkout_details['state'])

        checkout.enter_card_number('iframe[id^="card-fields-number"]', checkout_details['card_number'])
        checkout.enter_card_security_code('iframe[id^="card-fields-verification_value"]', checkout_details['card_cvc'])
        checkout.enter_card_expiry_date('iframe[id^="card-fields-expiry"]', checkout_details['card_expiry'])
        checkout.check_consent_checkbox()
        checkout.click_complete_order()
        return checkout.get_order_confirmation()

    def test_checkout_with_success_akk(self, driver):
        self.select_product(driver, 'Akkermansia')
        self.set_product_option(driver, 'pendulum-akkermansia')
        self.set_cart_quantity(driver, '1')

        checkout_confirmation = self.set_checkout_information(driver, self.checkout_details)
        assert checkout_confirmation == 'Thank you, Adriana!'

    def test_checkout_with_success_gc(self, driver):
        self.select_product(driver, 'Glucose Control')
        self.set_product_option(driver, 'pendulum-glucose-control-2-og')
        self.set_cart_quantity(driver, '1')

        checkout_confirmation = self.set_checkout_information(driver, self.checkout_details)
        assert checkout_confirmation == 'Thank you, Adriana!'