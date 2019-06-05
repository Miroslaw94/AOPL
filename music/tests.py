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
        self.client.post('/nuty/dodaj/', data={'title': 'Muppets'})

        self.assertEqual(MusicNotes.objects.count(), 1)
        new_notes = MusicNotes.objects.first()
        self.assertEqual(new_notes.title, 'Muppets')

    def test_redirects_after_post(self):
        response = self.client.post('/nuty/dodaj/', data={'title': 'Muppets'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/nuty/')

    def test_displays_all_list_items(self):
        MusicNotes.objects.create(title='nr1')
        MusicNotes.objects.create(title='nr2')

        response = self.client.get('/nuty/')

        self.assertIn('nr1', response.content.decode())
        self.assertIn('nr2', response.content.decode())


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

        response = self.client.get('/nuty/1/')
        self.assertTemplateUsed(response, 'music_notes_details.html')
        self.assertIn('Muppets', response.content.decode())
