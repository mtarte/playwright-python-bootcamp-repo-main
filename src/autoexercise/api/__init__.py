from playwright.sync_api import Page


class LoginPage:
    # __int
    def __init__(self, page: Page) -> None:
        # Locators
        self.page = page
        self.username = page.locator("[data-qa=\"login-email\"]")
        self.password = page.locator("[data-qa=\"login-password\"]")
        self.login_button = page.locator("[data-qa=\"login-button\"]")

        self.login_credentials = page.locator("[data-qa=\"login-credentials\"]")
        self.login_password = page.locator("[data-test=\"login-password\"]")
        self.error_message = page.locator("[data-test=\"error\"]")
        self.error_close_button = page.locator("[data-test=\"error-button\"]")