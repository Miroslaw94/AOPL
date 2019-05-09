from django.test import TestCase


class PageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_music_notes_template(self):
        response = self.client.get('/nuty/')
        self.assertTemplateUsed(response, 'music_notes.html')

    def test_uses_add_music_notes_template(self):
        response = self.client.get('/nuty/dodaj/')
        self.assertTemplateUsed(response, 'add_music_notes.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/nuty/dodaj/', data={'title': 'Muppets'})
        self.assertIn('Muppets', response.content.decode())
        self.assertTemplateUsed(response, 'music_notes.html')
