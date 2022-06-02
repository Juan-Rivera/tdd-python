from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Homepage
        self.browser.get('http://localhost:8000')

        # page title = To-Do
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Entering a to-do item
            # types "Buy peacock feathers" into text box
            # hits enter, page updates, page lists "1: Buy peacock feathers" as item in to-do list
        # Enters another to-do item
            # types "Use peacock feathers to make a fly"
            # hits enter, page updates, page lists both to-do items
        # visits unique generated URL
            # Check to-do list is still there

if __name__ == '__main__':
    unittest.main()