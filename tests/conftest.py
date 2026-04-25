import pytest
import os
from playwright.sync_api import sync_playwright

from utils.config import BASE_URL


@pytest.fixture(scope='session')
def browser():
    headed = os.getenv('HEADED', '0').lower() in ('1', 'true', 'yes')
    slow_mo_ms = int(os.getenv('SLOW_MO_MS', '0'))

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headed, slow_mo=slow_mo_ms)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()
