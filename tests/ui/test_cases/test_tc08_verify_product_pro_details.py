# Test cases 8: Verify Product Page Details. See https://automationexercise.com/test_cases

import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
    verify_products_page_visible,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

def test_tc08_verify_product_pro_details(app):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()

    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)

    # 4. Click on 'Products' button
    app.nav.products_link.click()

    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    # 6. The products list is visible
    verify_products_page_visible(app)

    # 7. Click on 'View Product' of first product
    app.products.open_product_details(app.products.cards.first)

    # 8. User is landed to product detail page
    assert "/product_details/1" in app.page.url

    # 9. Verify that detail is visible: product name, 
    # category, price, availability, condition, brand
    assert app.product_detail.name.is_visible()
    assert app.product_detail.label("Category:").is_visible()
    assert app.product_detail.price.is_visible()
    assert app.product_detail.label("Availability:").is_visible()
    assert app.product_detail.label("Condition:").is_visible()
    assert app.product_detail.label("Brand:").is_visible()