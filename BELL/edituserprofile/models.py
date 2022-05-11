from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EditProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, default="unknown")
    email = models.EmailField(max_length=255, default="unknown")
    country = models.CharField(max_length=255, default="unknown")
    bio = models.CharField(max_length=1000)
    profile_image = models.CharField(upload_to='images/', null=True, blank=True)
