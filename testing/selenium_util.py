import functools
import time
from selenium.webdriver.remote import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SlowWebdriver(webdriver.WebDriver):

    def execute(self, driver_command, params=None):
        time.sleep(0.5)
        return super(SlowWebdriver, self).execute(driver_command, params)

def with_driver(*desired_capabilities):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(test_case):
            for dc in desired_capabilities:
                driver = SlowWebdriver(
                    desired_capabilities=dc
                )

                # Opera YUNO maximize
                if dc is not DesiredCapabilities.OPERA:
                    driver.maximize_window()
                driver.implicitly_wait(10)

                try:
                    func(test_case, driver)
                finally:
                    driver.close()

        return wrapper

    return decorator
