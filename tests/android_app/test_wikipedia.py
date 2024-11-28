import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search(mobile_management):
    if mobile_management == "ios":
        pytest.skip("This test for android")

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_open_article(mobile_management):
    if mobile_management == "ios":
        pytest.skip("This test for android")

    with step('Open article'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/view_featured_article_card_article_title")).click()
