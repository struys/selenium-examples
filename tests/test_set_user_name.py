import testify as T
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from testing.selenium_util import with_driver


class TestApplication(T.TestCase):

	@with_driver(
		DesiredCapabilities.FIREFOX,
		DesiredCapabilities.CHROME
	)
	def test_set_user_name(self, driver):
		driver.get("http://localhost:5000")
		T.assert_equal(driver.find_element_by_tag_name('h1').text, 'Bob')
