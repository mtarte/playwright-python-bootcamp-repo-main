# Test case 7: Test Cases Page Verification. See https://automationexercise.com/test_cases

import pytest

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

def test_tc07_tc_pg_verification(app):
    # 1. Launch browser and navigate to the home page
    app.home.open()

    # 2. Click on the Test Cases button
    app.nav.test_cases_link.click()

    # 3. Verify that the Test Cases page is visible
    assert app.test_cases.heading.is_visible()

    # 4. Verify that user is navigated to test cases page successfully
    assert app.test_cases.heading.is_visible()