"""Test case for viewing category products"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]



def test_tc19_view_category_products(app):
    """Test case for viewing category products"""
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()
    verify_home_page_visible(app)

    # 3. Verify that categories are visible on left side bar
    assert app.sidebar.categories_heading.is_visible()

    # 4. Click on category (MEN, WOMEN, KIDS)
    app.sidebar.open_category("Women")

    # 5. Click on any subcategory link under category, for example: Dress
    app.sidebar.open_subcategory("Women", "Dress")

    # 6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
    app.products.section_title.wait_for(state="visible")

    assert "WOMEN - DRESS PRODUCTS" in app.products.section_title.inner_text().upper()
       
    # # 7. On left side bar, click on any sub-category link of 'Men' category
    # # Men → Tshirts

    app.sidebar.open_category("Men")
    app.sidebar.open_subcategory("Men", "Tshirts")

    # 8. Verify that user is navigated to that category page
    app.products.section_title.wait_for(state="visible")

    assert "MEN - TSHIRTS PRODUCTS" in \
    app.products.section_title.inner_text().upper()