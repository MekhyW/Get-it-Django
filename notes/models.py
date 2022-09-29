from tokenize import Name
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)
    color = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    def __str__(self):
        return '{}. {} #{}'.format(self.id, self.title, self.tag.name)