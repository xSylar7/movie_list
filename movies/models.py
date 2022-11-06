from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'movie name {self.title} description {self.description}'
