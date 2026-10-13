# Test Case 9: Search Product. See https://automationexercise.com/test_cases

import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
    verify_products_page_visible,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc09_search_product(app):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()

    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)

    # 4. Click on 'Products' button
    app.nav.products_link.click()

    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    verify_products_page_visible(app)

    # 6. Enter product name in search input and click search button
    searched_product = "Jeans"
    app.products.search(searched_product)

    # 7. Verify 'SEARCHED PRODUCTS' is visible
    assert app.products.searched_heading.is_visible()

    # 8. Verify all the products related to search are visible
    names = app.products.names.all_inner_texts()
    assert names, "Search should return at least one product"
    for name in names:
        assert searched_product.lower() in name.lower(), f"'{name}' \
        does not match '{searched_product}'"
