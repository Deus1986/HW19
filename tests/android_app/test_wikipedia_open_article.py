import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


def test_open_article(mobile_management):
    # if mobile_management == "ios":
    #     pytest.skip("This test for android")

    with step('Open article'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/view_featured_article_card_article_title")).click()
