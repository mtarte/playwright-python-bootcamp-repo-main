# Test Case 10: Verify Subscription in home page. See https://automationexercise.com/test_cases

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc10_homepage_subscription(app):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()

    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)

    # 4. Scroll down to footer
    app.footer.scroll_into_view()

    # 5. Verify text 'SUBSCRIPTION'
    assert app.footer.heading.is_visible()

    # 6. Enter email address in input field and click arrow button
    app.home.footer.subscribe("manjutarte@cuvox.de")

    # 7. Verify success message 'You have been successfully subscribed!' is visible
    assert app.home.footer.success_message.is_visible()
    # assert "You have been successfully subscribed!" in app.footer.success_message.inner_text()
