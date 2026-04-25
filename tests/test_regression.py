from pages.login_page import LoginPage
from utils.config import PASSWORD, USERNAME


def test_login_with_wrong_password(page):
    login_page = LoginPage(page)

    login_page.login(USERNAME, 'wrong_password')
    login_page.assert_error_visible('Username and password do not match')


def test_login_with_empty_username(page):
    login_page = LoginPage(page)

    login_page.login('', PASSWORD)
    login_page.assert_error_visible('Username is required')


def test_login_with_locked_user(page):
    login_page = LoginPage(page)

    login_page.login('locked_out_user', PASSWORD)
    login_page.assert_error_visible('Sorry, this user has been locked out')