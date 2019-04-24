from selenium import webdriver
import unittest
import time


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

    def test_add_music_notes(self):
        self.browser.get('http://localhost:8000/nuty/dodaj/')
        self.assertIn('AOPL', self.browser.title)

        name_input = self.browser.find_element_by_name('title')
        self.assertEqual(name_input.get_attribute('placeholder'), 'Enter a title')
        name_input.send_keys('Muppets')

        file_input = self.browser.find_element_by_name('file')
        self.assertEqual(file_input.get_attribute('name'), 'violin')
        file_input.send_keys('/Users/Miroslaw_Siwik/kodzenie/aopl/nuty_testowe.pdf')
        file_input.submit()
        time.sleep(1)

        self.browser.get('http://localhost:8000/nuty/')
        post = self.browser.find_element_by_tag_name('a')
        self.assertEqual(post.text, 'Muppets')
        self.assertEqual(post.get_attribute('href'), 'http://localhost:8000/nuty/<int:pk>')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
