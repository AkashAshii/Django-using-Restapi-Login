from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username




