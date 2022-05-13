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


def get_your_bids(user):
    list_of_items = []
    for x in Bids.objects.all().filter(bidder_id=user.id):
        item = ListItem.objects.get(id=x.item_id)
        try:
            itid = item.id
            itimage = item.main_image
            itname = item.itemname
            itrating = item.user.profile.rating
            ithighest = item.highest_bid
            bid = x.bid
            item = {'id': itid, 'image': itimage, 'name': itname, 'rating': itrating, 'highest': ithighest, 'bid': bid}
            list_of_items.append(item)

        except:
            pass

    return list_of_items
