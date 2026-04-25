from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import PASSWORD, USERNAME


def test_login_success(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login(USERNAME, PASSWORD)
    inventory_page.assert_products_page()
