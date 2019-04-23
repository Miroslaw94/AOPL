from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_open_site(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('AOPL', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Akademicka Orkiestra', header_text)
        self.fail('Finish the test!')

    def test_music_notes_site(self):
        self.browser.get('http://localhost:8000/nuty/')
        self.assertIn('AOPL', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Nuty', header_text)

        button = self.browser.find_element_by_tag_name('a')
        self.assertEqual('Dodaj nuty', button.text)
        self.assertEqual(button.get_attribute('href'), 'http://localhost:8000/nuty/dodaj/')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
