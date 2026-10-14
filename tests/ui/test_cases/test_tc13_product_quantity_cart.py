"""Test Case 13: Product Quantity in Cart: 
https://automationexercise.com/test_cases"""

import pytest

from tests.ui.conftest import home_page
from tests.ui.test_cases.steps import verify_home_page_visible, verify_products_page_visible

pytestmark = [pytest.mark.ui,pytest.mark.testcases]

def test_tc13_product_quantity_cart(app):

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'

    app.home.open()

#  3. Verify that home page is visible successfully  
    verify_home_page_visible(app)
     

#  # 4. Click 'View Product' for any product on home page
    app.products.open_product_details(app.products.cards.first)


#  5. Verify product detail is opened
    assert app.product_detail.info.is_visible()

#  6. Increase quantity to 4   
    app.product_detail.set_quantity(4)


# 7. Click 'Add to cart' button
    app.product_detail.add_to_cart()

# 8. Click 'View Cart' button
    app.product_detail.view_cart_from_modal()

# 9. Verify that product is displayed in cart page with exact quantity
    assert app.cart.rows.count() == 1
    assert app.cart.item_names.first.is_visible()
    assert app.cart.quantities.first.inner_text() == "4"


