from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import PASSWORD, PRODUCT_NAME, USERNAME


def test_add_product_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login(USERNAME, PASSWORD)
    inventory_page.assert_products_page()
    inventory_page.add_product_to_cart(PRODUCT_NAME)
    inventory_page.open_cart()

    cart_page.assert_item_visible(PRODUCT_NAME)
