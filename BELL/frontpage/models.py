from django.db import models

class Users(models.Model):
    user = models.CharField(max_length=255)