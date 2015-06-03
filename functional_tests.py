from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a new online to-do app. They go to checkout the
        # homepage.
        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "BUy peacock feathers" into a text box (They like to create
        # fly-fishing lures.

        # When she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list.

        # There  is still a text box inviting her to add another item. She enters "Use
        # peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # She sees that the site has generated a unique URL for her -- There is some
        # explantory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
