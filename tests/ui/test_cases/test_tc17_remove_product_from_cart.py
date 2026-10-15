import pytest
from playwright.sync_api import expect

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc17_remove_from_cart(app):
    # 1-2. Open homepage
    app.home.open()

    # 3. Verify homepage
    verify_home_page_visible(app)

    # 4. Add products to cart
    # Add first product
    app.home.add_card_to_cart(app.home.featured_items.nth(0))
    # app.home.continue_shopping()

    # # Add second product
    # app.home.add_card_to_cart(app.home.featured_items.nth(1))
    # app.home.view_cart_from_modal()

    app.home.view_cart_from_modal()
    assert app.cart.rows.count() == 1

    app.cart.remove_first_item()

    expect(
    app.page.locator(".cart_quantity_delete")).to_have_count(0, timeout=10000)
