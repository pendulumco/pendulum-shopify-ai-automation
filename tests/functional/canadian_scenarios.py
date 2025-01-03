import pytest

from page_objects.pages.cart import CartPage
from page_objects.pages.checkout_page import CheckoutPage
from page_objects.pages.home_page import HomePage
from constants import BASE_URL
from page_objects.pages.products_page import products_page


@pytest.mark.usefixtures("driver")
class TestCanadianScenarios:
    ALERT_MESSAGE = (
        "You have products in your cart that cannot be shipped to you. Due to Canadian import laws, "
        "we can only ship a maximum of 3 units of any of the following products: Akkermansia, Metabolic Daily, "
        "GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time purchase option or a 3-month supply "
        "membership of these items. At this time, we cannot ship Glucose Control internationally. If you have an "
        "item that isn't on the approved list, please remove it from your cart and proceed with checkout."
    )

    def select_product(self, driver, product):
        home_page = HomePage(driver)
        home_page.open_home_page(BASE_URL)
        home_page.click_shop_all_menu()
        home_page.select_product(product)

    def set_cart_quantity(self, driver, quantity):
        cart = CartPage(driver)
        cart.set_item_qtd(quantity)
        cart.click_continue_to_checkout()

    def set_checkout_values(self, driver, email, country):
        checkout = CheckoutPage(driver)
        checkout.enter_email(email)
        checkout.set_country(country)
        checkout.check_consent_checkbox()

    def get_canadian_alert(self, driver):
        checkout = CheckoutPage(driver)
        return checkout.get_canadian_alert()

    def set_product_option(self, driver, data_product):
        product = products_page(driver)
        product.set_radio_data_product(data_product)
        product.click_add_to_cart()
        product.click_close_upsell_modal()

    def test_Akkermansia_exceeds_allowed_quantity_for_Canadian_address(self, driver):
        self.select_product(driver, 'Akkermansia')
        self.set_product_option(driver, 'pendulum-akkermansia')
        self.set_cart_quantity(driver, '7')
        self.set_checkout_values(driver,'raian.damaceno@pendulum.co', 'CA')

        assert self.get_canadian_alert(driver) == self.ALERT_MESSAGE

    def test_Metabolic_Daily_exceeds_allowed_quantity_for_Canadian_address(self, driver):
        self.select_product(driver, 'Metabolic Daily')
        self.set_product_option(driver, 'pendulum-metabolic-daily-membership-90-count')
        self.set_cart_quantity(driver, '7')
        self.set_checkout_values(driver,'raian.damaceno@pendulum.co', 'CA')

        assert self.get_canadian_alert(driver) == self.ALERT_MESSAGE

    def test_Glucose_Control_not_available_for_Canadian_shipping(self, driver):
        self.select_product(driver, 'Glucose Control')
        self.set_product_option(driver, 'pendulum-glucose-control-2-og')
        self.set_cart_quantity(driver, '7')
        self.set_checkout_values(driver,'raian.damaceno@pendulum.co', 'CA')

        assert self.get_canadian_alert(driver) == self.ALERT_MESSAGE

    @pytest.mark.skip
    def test_Polyphenol_Booster_exceeds_allowed_quantity_for_Canadian_address(self, driver):
        self.select_product(driver, 'Polyphenol Booster')
        self.set_product_option(driver, 'polyphenol-booster-membership')
        self.set_cart_quantity(driver, '7')
        self.set_checkout_values(driver,'raian.damaceno@pendulum.co', 'CA')

        assert self.get_canadian_alert(driver) == self.ALERT_MESSAGE
