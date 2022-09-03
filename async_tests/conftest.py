import pytest_asyncio
from playwright.async_api import async_playwright

@pytest_asyncio.fixture
async def browser(browser_type_launch_args):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False,
                                             args=[*browser_type_launch_args])
        yield browser



@pytest_asyncio.fixture
async def context(browser):
    context = await browser.new_context(**{"timezone_id": "Europe/Helsinki",
                                     "viewport": {"width": 1920, "height": 1080}})
    yield context


@pytest_asyncio.fixture
async def page_object(context, url="http://127.0.0.1:8000"):
    page = await context.new_page()
    await page.goto(url)
    yield page
