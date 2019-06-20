from selenium import webdriver
from django.test import LiveServerTestCase
import unittest
import time

from music.models import MusicNotes
from aopl.settings import MEDIA_ROOT


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_open_site(self):
        self.browser.get(self.live_server_url)
        self.assertIn('AOPL', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Akademicka Orkiestra', header_text)
        self.fail('Finish the test!')

    def test_music_notes_site(self):
        self.browser.get(self.live_server_url + '/nuty/')
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Nuty', header_text)

        button1 = self.browser.find_element_by_tag_name('input')
        button2 = self.browser.find_element_by_tag_name('form')
        self.assertEqual('Dodaj nuty', button1.get_attribute('value'))
        self.assertEqual(button2.get_attribute('action'), self.live_server_url + '/nuty/dodaj/')

    def test_add_music_notes(self):
        self.browser.get(self.live_server_url + '/nuty/dodaj/')
        name_input = self.browser.find_element_by_name('title')
        name_input.send_keys('Muppets')

        file_input = self.browser.find_element_by_css_selector("input[type='file'][name='viola']")
        file_input.send_keys('/Users/Miroslaw_Siwik/kodzenie/aopl/nuty_testowe.pdf')
        self.browser.find_element_by_name('submit').click()
        time.sleep(1)

        posts = self.browser.find_elements_by_class_name('list-group-item')
        self.assertTrue(posts[0].text, 'Muppets')

        self.browser.get(posts[0].get_attribute('href'))
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Muppets', header_text)

    def test_delete_music_notes(self):
        MusicNotes.objects.create(title='Polonez')
        MusicNotes.objects.create(title='Muppets')
        MusicNotes.objects.create(title='Waltz')

        self.browser.get(self.live_server_url + '/nuty/')
        button = self.browser.find_elements_by_class_name('btn-danger')
        button[0].click()
        time.sleep(1)

        self.browser.find_element_by_name('submit').click()
        time.sleep(1)

        posts = self.browser.find_elements_by_class_name('list-group-item')
        self.assertTrue(posts[0].text, 'Muppets')
        self.assertTrue(posts[1].text, 'Waltz')
        self.assertNotIn('Polonez', MEDIA_ROOT)

    def test_edit_music_notes(self):
        MusicNotes.objects.create(title='Polonez')

        self.browser.get(self.live_server_url + '/nuty/')
        button = self.browser.find_elements_by_class_name('btn-warning')
        button[0].click()
        time.sleep(1)

        name_input = self.browser.find_element_by_name('title')
        name_input.clear()
        name_input.send_keys('Muppets')
        self.browser.find_element_by_name('submit').click()
        time.sleep(1)

        post = self.browser.find_element_by_class_name('list-group-item')
        self.assertTrue(post.text, 'Muppets')
        time.sleep(4)
