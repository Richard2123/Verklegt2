from django.db import models


class Purchase(models.Model):
    itemid = models.IntegerField()
    sellerid = models.IntegerField()
    buyerid = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.itemid} {self.sellerid} {self.buyerid} {self.price}"
