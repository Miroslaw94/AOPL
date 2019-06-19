import os
from django.db import models
from django.utils import timezone
from aopl.settings import MEDIA_ROOT


def file_path(instance, filename):
    return f'{instance}/{filename}'


class MusicNotes(models.Model):
    title = models.CharField(max_length=200, default='')

    score = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    piano = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    percussion = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    solo_instrument = models.FileField(default='', blank=True, null=True, upload_to=file_path)

    violin1 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    violin2 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    viola = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    cello = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    double_bass = models.FileField(default='', blank=True, null=True, upload_to=file_path)

    flute1 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    flute2 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    oboe = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    clarinet1 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    clarinet2 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    bassoon = models.FileField(default='', blank=True, null=True, upload_to=file_path)

    saxophone1 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    saxophone2 = models.FileField(default='', blank=True, null=True, upload_to=file_path)

    horn1 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    horn2 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    trumpet1 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    trumpet2 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    trombone1 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    trombone2 = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    tuba = models.FileField(default='', blank=True, null=True, upload_to=file_path)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def instruments(self):
        self.score.verbose_name = 'Partytura'
        self.piano.verbose_name = 'Fortepian'
        self.percussion.verbose_name = 'Perkusja'
        self.solo_instrument.verbose_name = 'Partia solowa'

        self.violin1.verbose_name = 'Skrzypce pierwsze'
        self.violin2.verbose_name = 'Skrzypce drugie'
        self.viola.verbose_name = 'Altówka'
        self.cello.verbose_name = 'Wiolonczela'
        self.double_bass.verbose_name = 'Kontrabas'

        self.flute1.verbose_name = 'Flet pierwszy'
        self.flute2.verbose_name = 'Flet drugi'
        self.oboe.verbose_name = 'Obój'
        self.clarinet1.verbose_name = 'Klarnet pierwszy'
        self.clarinet2.verbose_name = 'Klarnet drugi'
        self.bassoon.verbose_name = 'Fagot'

        self.saxophone1.verbose_name = 'Saksofon pierwszy'
        self.saxophone2.verbose_name = 'Saksofon drugi'

        self.horn1.verbose_name = 'Waltornia pierwsza'
        self.horn2.verbose_name = 'Waltornia druga'
        self.trumpet1.verbose_name = 'Trąbka pierwsza'
        self.trumpet2.verbose_name = 'Trąbka druga'
        self.trombone1.verbose_name = 'Puzon pierwszy'
        self.trombone2.verbose_name = 'Puzon drugi'
        self.tuba.verbose_name = 'Tuba'

        return [self.score, self.piano, self.percussion, self.solo_instrument, self.violin1, self.violin2, self.viola,
                self.cello, self.double_bass, self.flute1, self.flute2, self.oboe, self.clarinet1, self.clarinet2,
                self.bassoon, self.saxophone1, self.saxophone2, self.horn1, self.horn2, self.trumpet1, self.trumpet2,
                self.trombone1, self.trombone2, self.tuba]

    def delete(self, *args, **kwargs):
        instruments = [self.score, self.piano, self.percussion, self.solo_instrument, self.violin1, self.violin2, self.viola,
                self.cello, self.double_bass, self.flute1, self.flute2, self.oboe, self.clarinet1, self.clarinet2,
                self.bassoon, self.saxophone1, self.saxophone2, self.horn1, self.horn2, self.trumpet1, self.trumpet2,
                self.trombone1, self.trombone2, self.tuba]
        catalog = os.path.join(MEDIA_ROOT, self.title)

        if os.path.isdir(catalog):
            for i in instruments:
                i.delete()
            os.rmdir(catalog)
        super().delete(*args, **kwargs)
