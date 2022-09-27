from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    def __str__(self):
        return '{}. {}'.format(self.id, self.title)