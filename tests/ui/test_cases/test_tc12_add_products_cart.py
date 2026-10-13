"""
Test Case 12: Add Products in Cart
Test Description: This test case verifies the functionality of adding products to the cart.
"""

import pytest
from autoexercise.pages.app import App

from tests.ui.test_cases.steps import add_first_product_from_home, verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

def test_tc12_add_products_cart(app):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()

    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)

    # 4. Click 'Products' button
    app.nav.products_link.click()

    #5. Hover over first product and click 'Add to cart' & 6. Click 'Continue Shopping' button
    add_first_product_from_home(app)

    #7. Hover over second product and click 'Add to cart'
    app.products.add_to_cart(1,continue_shopping=False)
    

    #8. Click 'View Cart' button
    app.products.view_cart_from_modal()

    # 9. Verify both products are added to Cart
    assert app.cart.rows.count() == 2

    first = app.cart.rows.nth(0)
    second= app.cart.rows.nth(1)

    assert first.get_by_text("Blue Top").is_visible()
    assert second.get_by_text("Men Tshirt").is_visible()
    

    # 10. Verify their prices, quantity and total price

    # First product - Blue Top
    assert app.cart.unit_prices.nth(0).inner_text() == "Rs. 500"
    assert app.cart.quantities.nth(0).inner_text() == "1"
    assert app.cart.totals.nth(0).inner_text() == "Rs. 500"

    # Second product - Men Tshirt
    assert app.cart.unit_prices.nth(1).inner_text() == "Rs. 400"
    assert app.cart.quantities.nth(1).inner_text() == "1"
    assert app.cart.totals.nth(1).inner_text() == "Rs. 400"
