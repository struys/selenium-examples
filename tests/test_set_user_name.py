import testify as T
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from testing.selenium_util import with_driver


class TestApplication(T.TestCase):
    """Test that JavaScript correctly sets a username on the homepage page"""

    @with_driver(
        DesiredCapabilities.FIREFOX,
        DesiredCapabilities.CHROME
    )
    def test_set_user_name(self, driver):
        driver.get("http://localhost:5000")

        header_element = driver.find_element_by_tag_name('h1')

        T.assert_equal(header_element.text, 'Bob')
