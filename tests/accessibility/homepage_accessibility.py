import pytest
from constants import BASE_URL
from page_objects.pages.home_page import HomePage
from helpers.accessibility_helper import AccessibilityHelper

@pytest.mark.usefixtures("driver")
class TestHomePageAccessibility:
    def test_check_critical_accessibility(self, driver):
        homepage = HomePage(driver)
        homepage.open_home_page('https://24emkbxmmacy3y4l-17531043894.shopifypreview.com/products/glp-1-probiotic?view=rs_pdp_template_main#benefits')

        results = AccessibilityHelper.run_accessibility_check(
            driver,
            report_path='accessibility_report_design2.json',
            impact_levels=['critical', 'serious']
        )

        AccessibilityHelper.assert_no_critical_violations(results)