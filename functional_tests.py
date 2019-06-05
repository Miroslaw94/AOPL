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

        button1 = self.browser.find_element_by_tag_name('input')
        button2 = self.browser.find_element_by_tag_name('form')
        self.assertEqual('Dodaj nuty', button1.get_attribute('value'))
        self.assertEqual(button2.get_attribute('action'), 'http://localhost:8000/nuty/dodaj/')

    def test_add_music_notes(self):
        self.browser.get('http://localhost:8000/nuty/dodaj/')
        self.assertIn('AOPL', self.browser.title)

        name_input = self.browser.find_element_by_name('title')
        name_input.send_keys('Muppets')

        file_input = self.browser.find_element_by_css_selector("input[type='file'][name='viola']")
        file_input.send_keys('/Users/Miroslaw_Siwik/kodzenie/aopl/nuty_testowe.pdf')
        self.browser.find_element_by_name('submit').click()
        time.sleep(2)

        posts = self.browser.find_elements_by_class_name('list-group-item')
        self.assertTrue(posts[0].text, 'Muppets')

        self.browser.get(posts[0].get_attribute('href'))
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Muppets', header_text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
