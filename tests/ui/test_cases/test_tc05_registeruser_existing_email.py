# Test Case 5: Register User with existing email. See https://automationexercise.com/test_cases 

import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

def test_tc05_registeruser_existing_email(app, signup_user):
    
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()
    
    # 3. Verify that home page is visible successfully
    verify_home_page_visible(app)

    # 4. Click on 'Signup / Login' button
    app.nav.login_link.click()

    # 5. Verify that 'New User Signup!' is visible
    assert app.login.signup_heading.inner_text() == "New User Signup!"


    # 6. & 7Enter name and already registered email address
    app.login.start_signup("Vishrut", "vishruttarte@dayrep.com")


    # 8. Verify error 'Email Address already exist!' is visible
    assert app.login.signup_error.is_visible()