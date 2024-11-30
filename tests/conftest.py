import os
import time

import pydantic
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser

from project import config


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    browser_platform = config.browser_platform
    if browser_platform == "android":
        options = UiAutomator2Options().load_capabilities({
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",

            # Set URL of the application under test
            "app": config.app,

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",

                # Set your access credentials
                "userName": "bsuser_SzPCp5",
                "accessKey": "zUGJksMDo9pQrR7LF4zz"
            }
        })

        browser.config.driver = webdriver.Remote(config.remote_url, options=options)

    else:
        options = XCUITestOptions().load_capabilities({
            # Specify device and os_version for testing
            "platformName": "ios",
            "platformVersion": "16",
            "deviceName": "iPhone 14",

            # Set URL of the application under test
            "app": config.app,

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "First Python project IOS",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test_ios",

                # Set your access credentials
                "userName": "bsuser_SzPCp5",
                "accessKey": "zUGJksMDo9pQrR7LF4zz"
            }
        })
        browser.config.driver = webdriver.Remote(config.remote_url, options=options)

    browser.config.timeout = config.timeout

    yield

    browser.quit()
