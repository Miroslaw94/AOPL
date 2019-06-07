from django import forms

from .models import MusicNotes


class NewMusicNotesForm(forms.ModelForm):

    class Meta:
        model = MusicNotes
        fields = ('title', 'score', 'piano', 'percussion', 'solo_instrument', 'violin1', 'violin2', 'viola', 'cello', 'double_bass',
                  'flute1', 'flute2', 'oboe', 'clarinet1', 'clarinet2', 'bassoon', 'saxophone1', 'saxophone2', 'horn1',
                  'horn2', 'trumpet1', 'trumpet2', 'trombone1', 'trombone2', 'tuba')
