import getpass
import testify as T
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from testing.selenium_util import with_driver

class TestRosi(T.TestCase):
	"""Test that a Student has graduated from U of T Computer Science"""

	@T.setup
	def get_rosi_pin(self):
		self.student_number = getpass.getpass("Student Number: ")
		self.pin = getpass.getpass("Rosi Pin: ")

	@with_driver(
		DesiredCapabilities.SAFARI
	)
	def test_my_degree(self, driver):
		driver.get("https://www.rosi.utoronto.ca")

		login_button = driver.find_element_by_css_selector('.rosi-login-content .first a')

		login_button.click()

		driver.find_element_by_css_selector('#personId').send_keys(self.student_number)
		driver.find_element_by_css_selector('#pin').send_keys(self.pin)

		driver.find_element_by_css_selector('#right input[value="Login"]').click()

		subject_posts = driver \
			.find_elements_by_class_name('menuitem')[6] \
			.find_element_by_css_selector('a')

		subject_posts.click()

		subject_post_table = driver.find_element_by_css_selector('.decorated')

		T.assert_equal(
			subject_post_table.find_elements_by_css_selector('td')[3].text,
			'SP CSC: SOFTWARE ENGINEERING'
		)

		T.assert_equal(
			subject_post_table.find_element_by_css_selector('.note-green').text,
			'Complete'
		)
