"""test case for registering at checkout"""

import pytest

from autoexercise.data import build_card
from tests.ui.test_cases.steps import (
    add_first_product_from_home,
    delete_account_through_ui,
    place_order_and_pay,
    sign_up_through_ui,
    verify_address_and_review,
    verify_home_page_visible,
    verify_logged_in_as,
)


@pytest.mark.ui
@pytest.mark.testcases
def test_tc14_register_at_checkout(app, signup_user):
    """test case for registering at checkout"""
#    1. Launch browser
#    2. Navigate to url 'http://automationexercise.com'
    app.home.open()
    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)

    # 4. Add products to cart
    product_name = add_first_product_from_home(app)
    
    # 5. Click 'Cart' button
    app.home.nav.cart_link.click()

    # 6. Verify that cart page is displayed
   

    # 7. Click 'Proceed To Checkout' button
    app.cart.proceed_to_checkout()

   # 8. Click 'Register / Login' button
    app.cart.register_login_link.click()

    # 9. Fill all details in Signup and create account 
    # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    sign_up_through_ui(app, signup_user)
    
    # 11. Verify ' Logged in as username' at top    
    verify_logged_in_as(app, signup_user["name"]) 

     # 12.Click 'Cart' button
    app.home.nav.cart_link.click()

    # 13. Click 'Proceed To Checkout' button
    app.cart.proceed_to_checkout()

    # 14. Verify Address Details and Review Your Order
    verify_address_and_review(app, signup_user, product_name)


    # 15-18. Place the order, pay, and verify successful confirmation
    place_order_and_pay(
        app,
        build_card(),
        comment="Please deliver my order carefully.",
    )
    
    # 19. Click 'Delete Account' button
    delete_account_through_ui(app)
    
   