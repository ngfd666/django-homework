from django.db import models
from django.contrib.auth.models import User


class NoteManager(models.Manager):
    def create_note(self, title, text, owner):
        note = self.create(title=title, text=text, owner=owner)

        return note


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    objects = NoteManager()
