# Test Case 6: Contact Us. See https://automationexercise.com/test_cases

from pathlib import Path

import pytest
from autoexercise.pages.app import App
from autoexercise.pages.contact_page import ContactPage

from tests.ui import test_cases
from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)
pytestmark = [pytest.mark.ui, pytest.mark.testcases]

def test_tc06_contact_us(app, signup_user):
    
    # 1. Launch browser and navigate to the home page
    app.home.open()

    # 2. Click on the Contact Us button
    app.nav.contact_link.click()

    # 3. Verify that the Contact Us page is visible
    assert app.contact.heading.is_visible()

    # 4. Enter name, email, 
    # subject and message 
    # 5. Upload a file  
    # 6. Click on the Submit button

    upload_file = Path(__file__).parent / "test_data" / "test_file.txt.rtf"
    app.contact.submit("Vishrut", "vishruttarte@dayrep.com", "Contact Info", "This is a test message", file_path=upload_file)
    
    # 7. Verify that success message 'Success! Your details have been submitted successfully.' is visible
    assert app.contact.success_message.is_visible()

    # 8. Click on the Home button   
    app.contact.home_button.click()
    assert app.home.recommended_heading.is_visible()

    