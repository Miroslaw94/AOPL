from django.db import models
from django.utils import timezone


def file_path(instance, filename):
    return f'{instance}'


class MusicNotes(models.Model):
    title = models.CharField(max_length=200, default='')
    viola = models.FileField(default='', blank=True, null=True, upload_to=file_path)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
