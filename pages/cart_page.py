from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkout_button = page.get_by_role('button', name='Checkout')

    def assert_item_visible(self, product_name: str) -> None:
        expect(self.page.locator('.cart_item')).to_contain_text(product_name)

    def remove_product(self, product_name: str) -> None:
        cart_item = self.page.locator('.cart_item').filter(has_text=product_name)
        cart_item.get_by_role('button', name='Remove').click()

    def checkout(self) -> None:
        self.checkout_button.click()
