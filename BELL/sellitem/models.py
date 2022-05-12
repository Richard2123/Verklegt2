from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
"""from storages.backends.gcloud import GoogleCloudStorage
storage = GoogleCloudStorage()"""


"""class Upload:
    @staticmethod
    def upload_item_image(image, name):
        try:
            target_path = '/images/' + name
            location = storage.save(target_path, image)
            return storage.url(location)
        except Exception as x:
            print("Image could not be uploaded")"""


class ListItem(models.Model):
    itemname = models.CharField(max_length=255)
    condition = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    base_price = models.FloatField(default=0)
    main_image = models.CharField(max_length=9999, null=True, blank=True)
    image2 = models.CharField(max_length=9999, null=True, blank=True)
    image3 = models.CharField(max_length=9999, null=True, blank=True)
    image4 = models.CharField(max_length=9999, null=True, blank=True)
    image5 = models.CharField(max_length=9999, null=True, blank=True)

    def __str__(self):
        return f"{self.itemname}  {self.condition} {self.description}"

    def __float__(self):
        return self.base_price


def get_frontpage_listings():
    list_of_items = []
    for x in ListItem.objects.all()[:6]:
        try:
            itimage = x.main_image
            itname = x.itemname
            itrating = 'unknown'
            ithighest = '10'
            item = {'image': itimage, 'name': itname, 'rating': itrating, 'highest': ithighest}
            list_of_items.append(item)

        except:
            pass

    return list_of_items
