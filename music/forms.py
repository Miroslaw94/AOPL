from django import forms

from .models import MusicNotes


class NewMusicNotesForm(forms.ModelForm):

    class Meta:
        model = MusicNotes
        fields = ('title', 'violin', 'viola')
