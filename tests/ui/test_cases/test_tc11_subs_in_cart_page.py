"""Test case 11: Subscribe in Cart Page"""
import pytest
from autoexercise.pages.app import App
from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


@pytest.mark.ui

def test_tc11_subs_in_cart_page(app):
    
    # 1.Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()
    
    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)
    
    # 4. Click on 'Cart' button
    app.nav.cart_link.click()
   
    # 5. Verify that cart page is displayed
    assert app.cart.path == "/view_cart"

    # 5. Scroll down to footer
    # 6. Verify text 'SUBSCRIPTION'
    assert app.home.footer.heading.is_visible()
    assert app.home.footer.heading.inner_text() == "Subscription"
    
    # 7.Enter email address in input and click arrow button
    app.home.footer.subscribe("test11@test.com")
    
    # 8. Verify success message 'You have been 
    # successfully subscribed!' is visible
    assert app.home.footer.success_message.is_visible()