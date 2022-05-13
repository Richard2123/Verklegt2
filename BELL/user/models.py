from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=400, blank=True)
    country = CountryField(max_length=4000, blank_label='(select country)', blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    image = models.CharField(max_length=9999, blank=True, default="https://cdn.vectorstock.com/i/1000x1000/45/79/male-avatar-profile-picture-silhouette-light-vector-4684579.webp")
    rating = models.CharField(max_length=3, null=True)

    def __str__(self):
        return f"{self.user} {self.full_name} {self.email} {self.country} {self.bio} {self.image}"

    def __int__(self):
        return self.id
