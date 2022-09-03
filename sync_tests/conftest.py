import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser(browser_type_launch_args):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False,
                                             args=[*browser_type_launch_args])
        yield browser



@pytest.fixture
def context(browser):
    context = browser.new_context(**{"timezone_id": "Europe/Helsinki",
                                     "viewport": {"width": 1920, "height": 1080}})
    yield context


@pytest.fixture
def page_object(context, url="http://127.0.0.1:8000"):
    page = context.new_page()
    page.goto(url)
    yield page
