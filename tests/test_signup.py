import testify as T
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from testing.selenium_util import with_driver

class TestApplication(T.TestCase):

	@with_driver(
		DesiredCapabilities.FIREFOX,
		DesiredCapabilities.CHROME
	)
	def test_signup(self, driver):
		driver.get("http://localhost:5000/signup")

		signup_form = driver.find_element_by_css_selector('.signup-form')

		signup_form.find_element_by_name('name').send_keys('Ken')
		signup_form.find_element_by_name('email').send_keys('kstruys@yelp.com')
		signup_form.find_element_by_name('password').send_keys('mypassword')

		signup_form.find_element_by_tag_name('button').click()

		T.assert_equals(
			driver.find_element_by_css_selector('.success').text,
			"User is Signed up!"
		)

