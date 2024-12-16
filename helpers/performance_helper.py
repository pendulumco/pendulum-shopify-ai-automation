import json
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class PerformanceHelper:
    @staticmethod
    def capture_performance_metrics(driver, report_path='performance_report.json'):
        # Ensure the driver has performance logging enabled
        if not driver.capabilities.get('goog:loggingPrefs'):
            raise RuntimeError("Performance logging is not enabled for this WebDriver instance.")

        # Collect performance logs
        logs = driver.get_log('performance')
        performance_metrics = [json.loads(log['message'])['message'] for log in logs]

        # Save the performance metrics to the specified path
        report_dir = os.path.dirname(report_path)
        os.makedirs(report_dir, exist_ok=True)

        with open(report_path, 'w', encoding='utf-8') as report_file:
            json.dump(performance_metrics, report_file, indent=4)

        return performance_metrics

    @staticmethod
    def filter_navigation_timings(performance_metrics):
        navigation_timings = {}

        for metric in performance_metrics:
            if metric.get('method') == 'Page.loadEventFired':
                navigation_timings['loadEventFired'] = metric
            elif metric.get('method') == 'Page.domContentEventFired':
                navigation_timings['domContentLoaded'] = metric

        return navigation_timings

    @staticmethod
    def assert_performance_below_threshold(navigation_timings, load_time_threshold=2000, dom_content_threshold=1500):
        load_time = navigation_timings.get('loadEventFired', {}).get('timestamp', 0)
        dom_content_time = navigation_timings.get('domContentLoaded', {}).get('timestamp', 0)

        assert load_time <= load_time_threshold, f"Page load time exceeded: {load_time}ms (threshold: {load_time_threshold}ms)"
        assert dom_content_time <= dom_content_threshold, f"DOMContentLoaded time exceeded: {dom_content_time}ms (threshold: {dom_content_threshold}ms)"