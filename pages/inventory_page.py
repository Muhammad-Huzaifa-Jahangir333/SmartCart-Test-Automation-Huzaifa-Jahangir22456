import re

from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_link = page.locator('.shopping_cart_link')
        self.product_title = page.locator('.title')

    def assert_products_page(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*inventory\.html"))
        expect(self.product_title).to_have_text("Products")

    def add_product_to_cart(self, product_name: str) -> None:
        product_card = self.page.locator('.inventory_item').filter(has_text=product_name)
        product_card.get_by_role('button', name='Add to cart').click()

    def open_cart(self) -> None:
        self.cart_link.click()
