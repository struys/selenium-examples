import functools
import time
from selenium.webdriver.remote import webdriver

class SlowWebdriver(webdriver.WebDriver):

	def execute(self, driver_command, params=None):
		time.sleep(1)
		return super(SlowWebdriver, self).execute(driver_command, params)

def with_driver(*desired_capabilities):

	def decorator(func):

		@functools.wraps(func)
		def wrapper(test_case):
			for dc in desired_capabilities:
				driver = SlowWebdriver(
					desired_capabilities=dc
				)

				driver.implicitly_wait(10)

				try:
					func(test_case, driver)
				finally:
					driver.close()

		return wrapper

	return decorator