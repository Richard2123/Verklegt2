from django.db import models
from sellitem.models import ListItem
from django.contrib.auth.models import User
# Create your models here.


class Bids(models.Model):
    item = models.ForeignKey(ListItem, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.FloatField()

    def __int__(self):
        return self.item, self.bidder

    def __float__(self):
        return self.bid

