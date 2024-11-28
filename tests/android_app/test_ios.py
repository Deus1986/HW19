import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_ios(mobile_management):
    if mobile_management == "android":
        pytest.skip("This test for ios")
    with allure.step("Click text button"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with allure.step("Type text"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).click().type("hello@browserstack.com" + "\n")

    with allure.step("Assert text output"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("hello@browserstack.com"))

