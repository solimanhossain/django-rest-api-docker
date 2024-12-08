from django.db import models

class Joke(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
