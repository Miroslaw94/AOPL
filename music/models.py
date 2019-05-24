from django.db import models


def file_path(instance, filename):
    return f'{instance}'


class MusicNotes(models.Model):
    title = models.CharField(max_length=200, default='')
    viola = models.FileField(default='', blank=True, null=True, upload_to=file_path)

    def __str__(self):
        return self.title
