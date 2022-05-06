from django.db import models
from django.contrib.postgres.fields import ArrayField


class Locations(models.Model):
    zip = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.zip}"


class People(models.Model):
    pname = models.CharField(max_length=255)
    location = models.ForeignKey(Locations, default=0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"{self.pname} {self.location}"


class ItemImage(models.Model):
    image = models.ImageField(upload_to="images/")



class Item(models.Model):
    name = models.CharField(max_length=255)
    userid = models.IntegerField()
    user_rank = models.CharField(max_length=255, blank=True)
    starting_price = models.FloatField()
    first_image = models.ForeignKey(ItemImage, default=0, on_delete=models.SET_DEFAULT)
    images = ArrayField(models.IntegerField())



