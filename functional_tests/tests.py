from selenium import webdriver
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
import time

from music.models import MusicNotes
from aopl.settings import MEDIA_ROOT


class FunctionsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        User.objects.create_superuser(username='test', email='test@test.com', password='qwerty')

        self.browser.get(self.live_server_url + '/login/')
        username_input = self.browser.find_element_by_name('username')
        username_input.send_keys('test')
        password_input = self.browser.find_element_by_name('password')
        password_input.send_keys('qwerty')
        self.browser.find_element_by_name('submit').click()

    def tearDown(self):
        self.browser.quit()

    def test_open_site(self):
        self.browser.get(self.live_server_url)
        self.assertIn('AOPL', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Akademicka Orkiestra', header_text)

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
        name_input.send_keys('test')

        file_input = self.browser.find_element_by_css_selector("input[type='file'][name='viola']")
        file_input.send_keys('/Users/Miroslaw_Siwik/kodzenie/aopl/nuty_testowe.pdf')
        self.browser.find_element_by_name('submit').click()
        time.sleep(1)

        posts = self.browser.find_elements_by_class_name('list-group-item')
        self.assertIn('test', posts[0].text)

        self.browser.get(posts[0].get_attribute('href'))
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('test', header_text)

    def test_delete_music_notes(self):
        MusicNotes.objects.create(title='test1')
        MusicNotes.objects.create(title='test2')
        MusicNotes.objects.create(title='test3')

        self.browser.get(self.live_server_url + '/nuty/')
        button = self.browser.find_elements_by_class_name('btn-danger')
        button[0].click()
        time.sleep(1)

        self.browser.find_element_by_name('submit').click()
        time.sleep(1)

        posts = self.browser.find_elements_by_class_name('list-group-item')
        self.assertIn('test2', posts[0].text)
        self.assertIn('test1', posts[1].text)
        self.assertNotIn('test3', MEDIA_ROOT)

    def test_edit_music_notes(self):
        MusicNotes.objects.create(title='Title')

        self.browser.get(self.live_server_url + '/nuty/')
        button = self.browser.find_elements_by_class_name('btn-warning')
        button[0].click()
        time.sleep(1)

        name_input = self.browser.find_element_by_name('title')
        name_input.clear()
        name_input.send_keys('New_title')

        self.browser.find_element_by_name('submit').click()
        time.sleep(1)

        post = self.browser.find_element_by_class_name('list-group-item')
        self.assertIn('New_title', post.text)

    def test_parts_only_for_users(self):
        self.browser.get(self.live_server_url + '/logout/')
        navbar_items = self.browser.find_elements_by_class_name('nav-item')
        for item in navbar_items:
            self.assertNotEqual('Nuty', item.text)

        self.browser.get(self.live_server_url + '/nuty/')
        self.assertEqual(self.live_server_url + '/login/?next=/nuty/', self.browser.current_url)

        self.browser.get(self.live_server_url + '/nuty/dodaj/')
        self.assertEqual(self.live_server_url + '/login/?next=/nuty/dodaj/', self.browser.current_url)
