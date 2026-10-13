# Test Case 10: Verify Subscription in home page. See https://automationexercise.com/test_cases

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc10_homepage_subscription(app):
    
    
    # 1-2. Open homepage
    app.home.open()
    # 3. Verify homepage
    verify_home_page_visible(app)
    # 4. Scroll down to footer
    app.home.footer.scroll_into_view()
    # 5. Verify text 'SUBSCRIPTION'
    assert app.home.footer.heading.is_visible()
    assert app.home.footer.heading.inner_text() == "SUBSCRIPTION"
    # 6. Enter email address in input and click arrow button
    app.home.footer.subscribe("test10@test.com")
    # 7. Verify success message 'You have been successfully subscribed!' is visible
    assert app.home.footer.success_message.is_visible()