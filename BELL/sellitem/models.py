from django.db import models
from django.contrib.auth.models import User


class ListItem(models.Model):
    itemname = models.CharField(max_length=255)
    condition = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    base_price = models.FloatField(default=0)
    main_image = models.CharField(max_length=9999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image2 = models.CharField(max_length=9999, null=True, blank=True)
    image3 = models.CharField(max_length=9999, null=True, blank=True)
    image4 = models.CharField(max_length=9999, null=True, blank=True)
    image5 = models.CharField(max_length=9999, null=True, blank=True)
    sold = models.BooleanField(default=False)
    highest_bid = models.CharField(max_length=255, default=0)

    def __str__(self):
        return f"{self.itemname}  {self.condition} {self.description}"

    def __float__(self):
        return self.base_price, self.id,


def get_frontpage_listings():
    list_of_items = []
    for x in ListItem.objects.all().filter(sold=False):
        try:
            itid = x.id
            itimage = x.main_image
            itname = x.itemname
            itrating = 'unknown'
            ithighest = x.highest_bid
            iturl = '/itemdetail/'+str(itid)+'/'
            item = {'id': itid, 'image': itimage, 'name': itname, 'rating': itrating, 'highest': ithighest, 'url': iturl}
            list_of_items.append(item)

        except:
            pass

    return list_of_items


def get_your_items(user):
    list_of_items = []
    for x in ListItem.objects.all().filter(user_id=user.id)[:8]:
        try:
            itimage = x.main_image
            itname = x.itemname
            itrating = 'unknown'
            ithighest = x.highest_bid
            item = {'image': itimage, 'name': itname, 'rating': itrating, 'highest': ithighest}
            list_of_items.append(item)

        except:
            pass
    return list_of_items


def get_specific_item(itemid):
    return_item = {}
    item = ListItem.objects.get(itemid)
    try:
        itid = item.id
        itimage = item.main_image
        itname = item.itemname
        itrating = 'unknown'
        ithighest = item.highest_bid
        itemseller = item.user_id
        return_item = {'id': itid, 'image': itimage, 'name': itname, 'rating': itrating, 'highest': ithighest, 'seller': itemseller}

    except:
        pass

    return return_item
