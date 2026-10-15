"""test case for placing an order after logging in before checkout"""
import pytest

from autoexercise.data import build_card
from tests.ui.test_cases.steps import (
    add_first_product_from_home,
    delete_account_through_ui,
    place_order_and_pay,
    verify_home_page_visible,
    verify_logged_in_as,
)


@pytest.mark.ui
@pytest.mark.testcases
def test_tc16_place_order_login_before_checkout(app,new_user):
    """test case for placing an order after logging in before checkout"""
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()

    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)

    # 4. Click 'Signup / Login' button
    app.nav.login_link.click()

    # 5. Fill email address and password
    app.login.login(new_user["email"], new_user["password"])

    # 6. Verify 'Logged in as username' at top
    verify_logged_in_as(app, new_user["name"])

    # 7. Add products to cart
    add_first_product_from_home(app)

    # 8. Click 'Cart' button
    app.nav.cart_link.click()

    # 9. Verify that cart page is displayed
    assert app.page.url.endswith("/view_cart")
    assert "Blue Top" in app.cart.item_names.first.inner_text()
    
    # 10. Click 'Proceed To Checkout' button
    app.page.get_by_text("Proceed To Checkout", exact=True).click()

    # Verify navigation
    app.page.wait_for_url("**/checkout", timeout=15000)

    assert app.page.url.endswith("/checkout"), \
    "User did not navigate to checkout page"    

    # 11. Verify checkout page
    assert app.page.url.endswith("/checkout"), \
        "Checkout page not displayed"

    # 12. Verify delivery address
    assert app.checkout.delivery_address.is_visible(), \
        "Delivery address not displayed"

    # # 10. Click 'Proceed To Checkout' button
    # app.cart.proceed_to_checkout()

    # # 11. Verify Address Details and Review Your Order
    # verify_address_and_review(app, new_user, "Blue Top")

    # 12-15. Place the order, payment,confirm order and verify successful confirmation
    place_order_and_pay(app,card=build_card(), comment="Please deliver in the morning.")
    # assert app.order.heading.inner_text() == "Order Placed!"

    # 16. Click 'Delete Account' button and 17. verify 'ACCOUNT DELETED!'
    delete_account_through_ui(app)
   
    