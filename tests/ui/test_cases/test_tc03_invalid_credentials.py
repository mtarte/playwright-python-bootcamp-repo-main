# Test Case 3: Login User with incorrect email and password. see :https://automationexercise.com/test_cases 
import email
from hmac import new
import re

import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc03_invalid_credentials(app,new_user):
    
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()
    
    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)   

    # 4. Click on 'Signup / Login' button
    app.nav.login_link.click()

    # 5. Verify 'Login to your account' is visible
    assert app.login.login_heading.inner_text() == "Login to your account"

    # 6. & 7. Enter incorrect email address and password
    app.login.login(new_user["email"],"wrongpassword")


    # 8. Verify error 'Your email or password is incorrect!' is visible
    assert app.login.error_message.inner_text() == "Your email or password is incorrect!"



   


