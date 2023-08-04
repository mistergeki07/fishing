from django.db import models


class Login(models.Model):
    email = models.TextField()
    password = models.TextField()

