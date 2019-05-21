from django.db import models


class MusicNotes(models.Model):
    title = models.CharField(max_length=200, default='')
    viola = models.FileField(default='', blank=True, null=True)

    def __str__(self):
        return self.title
