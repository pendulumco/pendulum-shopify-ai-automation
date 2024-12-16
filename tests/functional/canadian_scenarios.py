import time

import pytest

from page_objects.pages.akkermansia_page import AkkermansiaPage
from page_objects.pages.cart import CartPage
from page_objects.pages.checkout_page import CheckoutPage
from page_objects.pages.glucose_control_page import GlucoseControlPage
from page_objects.pages.home_page import HomePage
from page_objects.pages.glp1_page import GLP1Page
from constants import BASE_URL
from page_objects.pages.metabolic_daily_page import MetabolicDailyPage
from page_objects.pages.polyphenol_page import polyphenol_page


@pytest.mark.usefixtures("driver")
class TestCanadianScenarios:
    # def test_GLP1_exceeds_allowed_quantity_for_Canadian_address(self, driver):
    #     home_page = HomePage(driver)
    #     home_page.open_home_page(BASE_URL)
    #     home_page.click_shop_all_menu()
    #     home_page.click_glp1_option()
    #
    #     glp1 = GLP1Page(driver)
    #     glp1.set_3months()
    #     glp1.click_add_to_cart()
    #     glp1.click_close_upsell_modal()
    #
    #     cart = CartPage(driver)
    #     cart.click_item_qtd()
    #     cart.set_item_qtd(7)
    #     cart.click_continue_to_checkout()
    #
    #     checkout = CheckoutPage(driver)
    #     checkout.enter_email('test@raian.com')
    #     checkout.click_country_dropdown()
    #     checkout.set_country('CA')
    #     test = checkout.get_canadian_alert()
    #     assert test == "You have products in your cart that cannot be shipped to you. Due to Canadian import laws, we can only ship a maximum of 3 units of any of the following products: Akkermansia, Metabolic Daily, GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time purchase option or a 3-month supply membership of these items. At this time, we cannot ship Glucose Control internationally. If you have an item that isn't on the approved list, please remove it from your cart and proceed with checkout."

    def test_Akkermansia_exceeds_allowed_quantity_for_Canadian_address(self, driver):
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
        cart.set_item_qtd(7)
        cart.click_continue_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_email('test@raian.com')
        checkout.click_country_dropdown()
        checkout.set_country('CA')
        checkout.check_consent_checkbox()

        test = checkout.get_canadian_alert()
        assert test == "You have products in your cart that cannot be shipped to you. Due to Canadian import laws, we can only ship a maximum of 3 units of any of the following products: Akkermansia, Metabolic Daily, GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time purchase option or a 3-month supply membership of these items. At this time, we cannot ship Glucose Control internationally. If you have an item that isn't on the approved list, please remove it from your cart and proceed with checkout."

    def test_Metabolic_Daily_exceeds_allowed_quantity_for_Canadian_address(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page(BASE_URL)
        home_page.click_shop_all_menu()
        home_page.click_md_option()

        MD = MetabolicDailyPage(driver)
        MD.set_3months()
        MD.click_add_to_cart()
        MD.click_close_upsell_modal()

        cart = CartPage(driver)
        cart.click_item_qtd()
        cart.set_item_qtd(7)
        cart.click_continue_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_email('test@raian.com')
        checkout.click_country_dropdown()
        checkout.set_country('CA')
        checkout.check_consent_checkbox()

        test = checkout.get_canadian_alert()
        assert test == "You have products in your cart that cannot be shipped to you. Due to Canadian import laws, we can only ship a maximum of 3 units of any of the following products: Akkermansia, Metabolic Daily, GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time purchase option or a 3-month supply membership of these items. At this time, we cannot ship Glucose Control internationally. If you have an item that isn't on the approved list, please remove it from your cart and proceed with checkout."

    def test_Glucose_Control_not_available_for_Canadian_shipping(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page(BASE_URL)
        home_page.click_shop_all_menu()
        home_page.click_gc_option()

        gc = GlucoseControlPage(driver)
        gc.set_1month()
        gc.click_add_to_cart()
        gc.click_close_upsell_modal()

        cart = CartPage(driver)
        cart.click_item_qtd()
        cart.set_item_qtd(7)
        cart.click_continue_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_email('test@raian.com')
        checkout.click_country_dropdown()
        checkout.set_country('CA')
        checkout.check_consent_checkbox()

        test = checkout.get_canadian_alert()
        assert test == "You have products in your cart that cannot be shipped to you. Due to Canadian import laws, we can only ship a maximum of 3 units of any of the following products: Akkermansia, Metabolic Daily, GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time purchase option or a 3-month supply membership of these items. At this time, we cannot ship Glucose Control internationally. If you have an item that isn't on the approved list, please remove it from your cart and proceed with checkout."

    def test_Polyphenol_Booster_exceeds_allowed_quantity_for_Canadian_address(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page(BASE_URL)
        home_page.click_shop_all_menu()
        home_page.click_poly_option()

        poly = polyphenol_page(driver)
        poly.set_1month()
        poly.click_add_to_cart()
        poly.click_close_upsell_modal()

        cart = CartPage(driver)
        cart.click_item_qtd()
        cart.set_item_qtd(7)
        cart.click_continue_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_email('test@raian.com')
        checkout.click_country_dropdown()
        checkout.set_country('CA')
        checkout.check_consent_checkbox()

        test = checkout.get_canadian_alert()
        assert test == ("You have products in your cart that cannot be shipped to you. Due to Canadian import laws, "
                        "we can only ship a maximum of 3 units of any of the following products: Akkermansia, "
                        "Metabolic Daily, GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time "
                        "purchase option or a 3-month supply membership of these items. At this time, we cannot ship "
                        "Glucose Control internationally. If you have an item that isn't on the approved list, "
                        "please remove it from your cart and proceed with checkout.")

    # def test_GLP1_within_allowed_quantity_for_Canadian_address(self, driver):
    #     home_page = HomePage(driver)
    #     home_page.open_home_page(BASE_URL)
    #     home_page.click_shop_all_menu()
    #     home_page.click_glp1_option()
    #
    #     glp1 = GLP1Page(driver)
    #     glp1.set_3months()
    #     glp1.click_add_to_cart()
    #     glp1.click_close_upsell_modal()
    #
    #     cart = CartPage(driver)
    #     cart.click_item_qtd()
    #     cart.set_item_qtd(2)
    #     cart.click_continue_to_checkout()
    #
    #     checkout = CheckoutPage(driver)
    #     checkout.enter_email('test@raian.com')
    #     checkout.check_consent_checkbox()
    #     checkout.click_country_dropdown()
    #     checkout.set_country('CA')
    #     checkout.is_canadian_alert_absent()
    #
    # def test_Akkermansia_within_allowed_quantity_for_Canadian_address(self, driver):
    #     home_page = HomePage(driver)
    #     home_page.open_home_page(BASE_URL)
    #     home_page.click_shop_all_menu()
    #     home_page.click_Akkermansia_option()
    #
    #     AKK = AkkermansiaPage(driver)
    #     AKK.set_3months()
    #     AKK.click_add_to_cart()
    #     AKK.click_close_upsell_modal()
    #
    #     cart = CartPage(driver)
    #     cart.click_item_qtd()
    #     cart.set_item_qtd(2)
    #     cart.click_continue_to_checkout()
    #
    #     checkout = CheckoutPage(driver)
    #     checkout.enter_email('test@raian.com')
    #     checkout.click_country_dropdown()
    #     checkout.set_country('CA')
    #     checkout.is_canadian_alert_absent()
    #
    # def test_Metabolic_Daily_within_allowed_quantity_for_Canadian_address(self, driver):
    #     home_page = HomePage(driver)
    #     home_page.open_home_page(BASE_URL)
    #     home_page.click_shop_all_menu()
    #     home_page.click_md_option()
    #
    #     MD = MetabolicDailyPage(driver)
    #     MD.set_3months()
    #     MD.click_add_to_cart()
    #     MD.click_close_upsell_modal()
    #
    #     cart = CartPage(driver)
    #     cart.click_item_qtd()
    #     cart.set_item_qtd(2)
    #     cart.click_continue_to_checkout()
    #
    #     checkout = CheckoutPage(driver)
    #     checkout.enter_email('test@raian.com')
    #     checkout.click_country_dropdown()
    #     checkout.set_country('CA')
    #     test = checkout.get_canadian_alert()
    #     assert test == "You have products in your cart that cannot be shipped to you. Due to Canadian import laws, we can only ship a maximum of 3 units of any of the following products: Akkermansia, Metabolic Daily, GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time purchase option or a 3-month supply membership of these items. At this time, we cannot ship Glucose Control internationally. If you have an item that isn't on the approved list, please remove it from your cart and proceed with checkout."
    #
    # def test_Glucose_Control_within_allowed_quantity_for_Canadian_address(self, driver):
    #     home_page = HomePage(driver)
    #     home_page.open_home_page(BASE_URL)
    #     home_page.click_shop_all_menu()
    #     home_page.click_gc_option()
    #
    #     gc = GlucoseControlPage(driver)
    #     gc.set_1month()
    #     gc.click_add_to_cart()
    #     gc.click_close_upsell_modal()
    #
    #     cart = CartPage(driver)
    #     cart.click_item_qtd()
    #     cart.set_item_qtd(2)
    #     cart.click_continue_to_checkout()
    #
    #     checkout = CheckoutPage(driver)
    #     checkout.enter_email('test@raian.com')
    #     checkout.click_country_dropdown()
    #     checkout.set_country('CA')
    #     test = checkout.get_canadian_alert()
    #     assert test == ("You have products in your cart that cannot be shipped to you. Due to Canadian import laws, "
    #                     "we can only ship a maximum of 3 units of any of the following products: Akkermansia, Metabolic Daily, GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time purchase option or a 3-month supply membership of these items. At this time, we cannot ship Glucose Control internationally. If you have an item that isn't on the approved list, please remove it from your cart and proceed with checkout.")
    #
    # def test_Polyphenol_with_Canadian_address_(self, driver):
    #     home_page = HomePage(driver)
    #     home_page.open_home_page(BASE_URL)
    #     home_page.click_shop_all_menu()
    #     home_page.click_poly_option()
    #
    #     poly = polyphenol_page(driver)
    #     poly.set_1month()
    #     poly.click_add_to_cart()
    #     poly.click_close_upsell_modal()
    #
    #     cart = CartPage(driver)
    #     cart.click_item_qtd()
    #     cart.set_item_qtd(2)
    #     cart.click_continue_to_checkout()
    #
    #     checkout = CheckoutPage(driver)
    #     checkout.enter_email('test@raian.com')
    #     checkout.click_country_dropdown()
    #     checkout.set_country('CA')
    #     test = checkout.get_canadian_alert()
    #     assert test == "You have products in your cart that cannot be shipped to you. Due to Canadian import laws, we can only ship a maximum of 3 units of any of the following products: Akkermansia, Metabolic Daily, GLP-1 Probiotic, and Polyphenol Booster. You can choose the one-time purchase option or a 3-month supply membership of these items. At this time, we cannot ship Glucose Control internationally. If you have an item that isn't on the approved list, please remove it from your cart and proceed with checkout."
    #
    #     time.sleep()