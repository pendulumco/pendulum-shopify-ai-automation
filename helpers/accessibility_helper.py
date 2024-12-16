import json
from axe_selenium_python import Axe

class AccessibilityHelper:
    @staticmethod
    def run_accessibility_check(driver, report_path='accessibility_report.json', impact_levels=None):
        axe = Axe(driver)
        axe.inject()
        results = axe.run()

        if impact_levels:
            filtered_violations = [
                violation for violation in results.get('violations', [])
                if violation.get('impact') in impact_levels
            ]
            results['violations'] = filtered_violations

        with open(report_path, 'w', encoding='utf-8') as report_file:
            json.dump(results, report_file, indent=4)

        return results

    @staticmethod
    def assert_no_critical_violations(results):
        critical_violations = [
            violation for violation in results.get('violations', [])
            if violation.get('impact') == 'critical'
        ]
        assert not critical_violations, f"Critical accessibility issues found: {critical_violations}"
