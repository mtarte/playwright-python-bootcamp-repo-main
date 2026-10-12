"""Test Case 1: Register User. See https://automationexercise.com/test_cases"""

import re

import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc01_register_user(app, signup_user):
    app.home.open()                                           # 1-2 open the site
    verify_home_page_visible(app)                             # 3
    
    app.nav.login_link.click()                                # 4
    assert app.login.login_heading.inner_text() == "Login to your account"  # 5

    app.nav.signup_link.click()
    assert app.login.new_user_signup_visible.is_visible()
    
    app.login.start_signup(signup_user["name"], signup_user["email"])  # 6-7
    assert app.signup.account_info_heading.is_visible()   # 8
    app.signup.fill_account(signup_user, newsletter=True, offers=True)  # 9-12
    app.signup.submit()                                       # 13
    heading_text = app.account.created_heading.inner_text()
    assert re.search(r"account created", heading_text, re.IGNORECASE)  # 14
    
    app.account.continue_button.click()                       # 15
    verify_logged_in_as(app, signup_user["name"])             # 16
    delete_account_through_ui(app)                            # 17-18
