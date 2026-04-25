from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import FIRST_NAME, LAST_NAME, PASSWORD, POSTAL_CODE, PRODUCT_NAME, USERNAME


def test_complete_checkout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login(USERNAME, PASSWORD)
    inventory_page.add_product_to_cart(PRODUCT_NAME)
    inventory_page.open_cart()
    cart_page.assert_item_visible(PRODUCT_NAME)
    cart_page.checkout()
    checkout_page.fill_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.continue_checkout()
    checkout_page.finish_order()

    checkout_page.assert_order_complete()
