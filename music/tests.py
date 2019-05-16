from django.test import TestCase
from music.models import MusicNotes


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


class MusicNotesModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        muppets = MusicNotes()
        muppets.title = 'Muppets'
        muppets.viola = '/Users/Miroslaw_Siwik/kodzenie/aopl/nuty_testowe.pdf'
        muppets.save()

        saved_notes = MusicNotes.objects.all()
        self.assertEqual(saved_notes.count(), 1)
        self.assertEqual(saved_notes[0].title, 'Muppets')
        self.assertEqual(saved_notes[0].viola, '/Users/Miroslaw_Siwik/kodzenie/aopl/nuty_testowe.pdf')
