import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.pages.akkermansia_page import AkkermansiaPage
from page_objects.pages.cart import CartPage
from page_objects.pages.checkout_page import CheckoutPage
from page_objects.pages.glucose_control_page import GlucoseControlPage
from page_objects.pages.home_page import HomePage
from page_objects.pages.glp1_page import GLP1Page
from constants import BASE_URL
from page_objects.pages.metabolic_daily_page import MetabolicDailyPage
from page_objects.pages.polyphenol_page import polyphenol_page
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestCanadianScenarios:
   def test_checkout_with_success_akk(self, driver):
    home_page = HomePage(driver)
    home_page.open_home_page(BASE_URL)
    home_page.click_shop_all_menu()
    home_page.click_Akkermansia_option()

    AKK = AkkermansiaPage(driver)
    AKK.set_3months()
    AKK.click_add_to_cart()
    AKK.click_close_upsell_modal()

    cart = CartPage(driver)
    cart.click_item_qtd()
    cart.set_item_qtd(1)
    cart.click_continue_to_checkout()

    checkout = CheckoutPage(driver)

    checkout.enter_email('raian.damaceno@pendulum.co')
    checkout.enter_first_name('Raian')
    checkout.enter_last_name('Damaceno')
    checkout.enter_address('Rancho Cucamonga High School Pool')
    checkout.enter_city('Rancho Cucamonga')
    checkout.enter_postal_code('91701')
    checkout.select_state_by_text('California')

    checkout.enter_card_number('iframe[id^="card-fields-number"]', '5502 0933 1268 9075')
    checkout.enter_card_security_code('iframe[id^="card-fields-verification_value"]', '123')
    checkout.enter_card_expiry_date('iframe[id^="card-fields-expiry"]', '1030')
    checkout.check_consent_checkbox()
    checkout.click_complete_order()
    time.sleep(100)



