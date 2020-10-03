import unittest
from selenium import webdriver
import page

# A class inheriting from the unittest module
class PythonOrgSearch(unittest.TestCase):
    # Think of __init__ but for test cases
    # Note: this will run for each test case
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.driver.get('http://www.python.org')

    # any function starting with test will automatically be run when we run the unit test

    def test_search_python(self):
        # Loads main page
        mainPage = page.MainPage(self.driver)
        # Asserts title matches expected title
        assert mainPage.is_title_matches() # the comma means do after assertion is done
        mainPage.search_text_element = "pycon"
        # Click go button to search for ^^ pycon
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        # Asserts whether or not results were found searching for pycon
        assert search_result_page.is_results_found()

    def not_a_test(self):
        print("This will not print")

    # Runs at the end of the test to clean up
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
