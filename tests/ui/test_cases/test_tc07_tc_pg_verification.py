# Test case 7: Test Cases Page Verification. See https://automationexercise.com/test_cases

import pytest
from autoexercise.pages.app import App
from autoexercise.pages.contact_page import ContactPage
from tests.ui import test_cases
from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)
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