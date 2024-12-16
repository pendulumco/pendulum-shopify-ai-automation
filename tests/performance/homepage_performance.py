import pytest
from helpers.performance_helper import PerformanceHelper
from constants import BASE_URL
from page_objects.pages.home_page import HomePage


@pytest.mark.usefixtures("driver")
class TestPerformance:
    def test_page_performance(self, driver):
        homepage = HomePage(driver)
        homepage.open_home_page(BASE_URL)

        # Capture performance metrics
        metrics = PerformanceHelper.capture_performance_metrics(driver, 'reports/performance/homepage_performance.json')

        # Extract and validate navigation timings
        timings = PerformanceHelper.filter_navigation_timings(metrics)
        PerformanceHelper.assert_performance_below_threshold(timings, load_time_threshold=3000, dom_content_threshold=2000)