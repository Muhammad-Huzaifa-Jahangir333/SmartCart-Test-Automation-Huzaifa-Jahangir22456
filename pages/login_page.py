from playwright.sync_api import Page, expect

from utils.config import BASE_URL


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def open(self) -> None:
        self.page.goto(BASE_URL)
        expect(self.page).to_have_title("Swag Labs")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_visible(self, message: str) -> None:
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(message)
