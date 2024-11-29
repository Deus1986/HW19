import os
import time

import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser

DEFAULT_PLATFORM = "android"


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action='store',
        default="android"
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    # browser_platform = request.config.getoption('--platform')
    # browser_platform = browser_platform if browser_platform != "" else DEFAULT_PLATFORM
    # if browser_platform == "android":
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

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
    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options
    b = browser.driver.session_id
    print(b)
    #
    # browser.config.timeout = float(os.getenv('timeout', '10.0'))
    #
    # yield "android"


# else:
#     options = XCUITestOptions().load_capabilities({
#         # Specify device and os_version for testing
#         "platformName": "ios",
#         "platformVersion": "16",
#         "deviceName": "iPhone 14",
#
#         # Set URL of the application under test
#         "app": "bs://sample.app",
#
#         # Set other BrowserStack capabilities
#         'bstack:options': {
#             "projectName": "First Python project IOS",
#             "buildName": "browserstack-build-1",
#             "sessionName": "BStack first_test_ios",
#
#             # Set your access credentials
#             "userName": "bsuser_SzPCp5",
#             "accessKey": "zUGJksMDo9pQrR7LF4zz"
#         }
#     })
#     browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
#     browser.config.driver_options = options
#
# browser.config.timeout = float(os.getenv('timeout', '10.0'))

# yield "ios"

# browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
# browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
    a = browser.driver.session_id
    print(a)
