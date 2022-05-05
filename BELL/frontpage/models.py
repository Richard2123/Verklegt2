from django.db import models

class Users(models.Model):
    user = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    user_rank = models.CharField(max_length=255, blank=True)
    price = models.FloatField()


class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

