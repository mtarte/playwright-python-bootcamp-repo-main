"""Test Case 2: Valid Credentials. See https://automationexercise.com/test_cases"""


import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]

# Test Case 2: Valid Credentials. See https://automationexercise.com/test_cases

def test_tc02_valid_credentials(app,new_user):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()     
    
    # 3.Verify that home page is visible successfully                                    
    verify_home_page_visible(app)                                    
    
    # 4.Click on 'Signup / Login' button
    app.nav.login_link.click()
     
    # 5. Verify that 'Logged in as username' is visible 
    assert app.login.login_heading.inner_text() == "Login to your account"

    # 6. & 7. Enter correct email address and password

    app.login.login(new_user["email"], new_user["password"])
    
    
    # 8. Verify that 'Logged in as username' is visible
    verify_logged_in_as(app,new_user["name"])
    
    # 9. & 10. Click 'Delete Account' button

    delete_account_through_ui(app)

   
            
