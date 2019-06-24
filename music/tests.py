from django.test import TestCase
from music.models import MusicNotes
from django.contrib.auth.models import User


class PageTestNormalUser(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@test.com', password='qwerty')
        self.client.force_login(self.user)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_music_notes_template(self):
        response = self.client.get('/nuty/')
        self.assertTemplateUsed(response, 'music_notes.html')

    def test_displays_all_list_items(self):
        MusicNotes.objects.create(title='nr1')
        MusicNotes.objects.create(title='nr2')

        response = self.client.get('/nuty/')

        self.assertIn('nr1', response.content.decode())
        self.assertIn('nr2', response.content.decode())

    def test_limited_access_if_logout(self):
        response = self.client.get('/nuty/')
        self.assertEqual(response.status_code, 200)

        self.client.logout()

        response = self.client.get('/nuty/')
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('Nuty', response.content.decode())
        self.assertTemplateNotUsed(response, 'music_notes.html')

    def test_limited_access_if_not_staff(self):
        response = self.client.get('/nuty/dodaj/')
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('Nuty', response.content.decode())


class PageTestStaffUser(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='test', email='test@test.com', password='qwerty')
        self.client.force_login(self.user)

    def test_uses_add_music_notes_template(self):
        response = self.client.get('/nuty/dodaj/')
        self.assertTemplateUsed(response, 'add_music_notes.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/nuty/dodaj/', data={'title': 'Test_item'})

        self.assertEqual(MusicNotes.objects.count(), 1)
        new_notes = MusicNotes.objects.first()
        self.assertEqual(new_notes.title, 'Test_item')

    def test_redirects_after_post(self):
        response = self.client.post('/nuty/dodaj/', data={'title': 'Test_item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/nuty/')


class MusicNotesModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='test', email='test@test.com', password='qwerty')
        self.client.force_login(self.user)

    def test_saving_and_retrieving_items(self):
        item1 = MusicNotes()
        item1.title = 'item1'
        item1.viola = '/Users/Miroslaw_Siwik/kodzenie/aopl/nuty_testowe.pdf'
        item1.save()

        saved_notes = MusicNotes.objects.all()
        self.assertEqual(saved_notes.count(), 1)
        self.assertEqual(saved_notes[0].title, 'item1')
        self.assertEqual(saved_notes[0].viola, '/Users/Miroslaw_Siwik/kodzenie/aopl/nuty_testowe.pdf')

        response = self.client.get('/nuty/1/')
        self.assertTemplateUsed(response, 'music_notes_details.html')
        self.assertIn('item1', response.content.decode())

    def test_deleting_items(self):
        item1 = MusicNotes()
        item1.title = 'item1'
        item1.save()
        item2 = MusicNotes()
        item2.title = 'item2'
        item2.save()

        saved_notes = MusicNotes.objects.all()
        self.assertEqual(saved_notes.count(), 2)

        item1.delete()

        self.assertEqual(saved_notes.count(), 1)
        self.assertEqual(saved_notes[0].title, 'item2')
