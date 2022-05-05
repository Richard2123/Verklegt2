from django.db import models


class Users(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)



class Item(models.Model):
    name = models.CharField(max_length=255)
    user_rank = models.CharField(max_length=255, blank=True)
    starting_price = models.FloatField()


class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

