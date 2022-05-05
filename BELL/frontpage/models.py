from django.db import models
from django.contrib.postgres.fields import ArrayField


class Locations(models.Model):
    zip = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)


class People(models.Model):
    pname = models.CharField(max_length=255)
    location = models.ForeignKey(Locations, default=0, on_delete=models.SET_DEFAULT)


class Users(models.Model):
    uuid = models.ForeignKey(People, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=9999, blank=True)


class ItemImage(models.Model):
    image = models.CharField(max_length=9999, blank=False,default=0)


class Item(models.Model):
    name = models.CharField(max_length=255)
    user_rank = models.CharField(max_length=255, blank=True)
    starting_price = models.FloatField()
    first_image = models.ForeignKey(ItemImage, default=0, on_delete=models.SET_DEFAULT)
    images = ArrayField(models.IntegerField())


