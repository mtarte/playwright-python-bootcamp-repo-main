"""test case for registering before checkout"""

import pytest
from autoexercise.data import build_card


from tests.ui.test_cases.steps import verify_home_page_visible
from tests.ui.test_cases.steps import sign_up_through_ui
from tests.ui.test_cases.steps import verify_logged_in_as
from tests.ui.test_cases.steps import verify_address_and_review
from tests.ui.test_cases.steps import place_order_and_pay
from tests.ui.test_cases.steps import delete_account_through_ui
from tests.ui.test_cases.steps import add_first_product_from_home


@pytest.mark.ui
@pytest.mark.testcases
def test_tc15_register_before_checkout(app,signup_user):
    """test case for registering before checkout"""
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()

    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)

    # 4. Click 'Signup / Login' button
    app.nav.login_link.click()

    # 5. Fill all details in Signup and create account & # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    sign_up_through_ui(app, signup_user)

    # 7. Verify 'Logged in as username' at top
    verify_logged_in_as(app, signup_user["name"])

    # 8. Add products to cart
    add_first_product_from_home(app)
    
    # 9. Click 'Cart' button
    app.nav.cart_link.click()
   
    # 10. Verify that cart page is displayed & 11. Click Proceed To Checkout
    assert app.page.url.endswith("/view_cart")  

    # 11. Click 'Proceed To Checkout' button
    app.cart.proceed_to_checkout()

    # 12. Verify Address Details and Review Your Order
    verify_address_and_review(app, signup_user, "Blue Top")

    # 13-15. Place the order, pay, and verify successful confirmation
    place_order_and_pay(app,card=build_card(), comment="Please deliver in the morning.")

    # 16. Click 'Delete Account' button and 17. verify 'ACCOUNT DELETED!'
    delete_account_through_ui(app)
    