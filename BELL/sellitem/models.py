from django.db import models
from django.contrib.postgres.fields import ArrayField
from storages.backends.gcloud import GoogleCloudStorage
storage = GoogleCloudStorage()


class Upload:
    @staticmethod
    def upload_item_image(image, name):
        try:
            target_path = '/images/' + name
            location = storage.save(target_path, image)
            return storage.url(location)
        except Exception as x:
            print("Image could not be uploaded")


class ListItem(models.Model):
    userid = models.IntegerField()
    itemname = models.CharField(max_length=255)
    condition = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    base_price = models.FloatField()
    main_image = models.IntegerField()
    other_images = ArrayField(models.IntegerField())


class ItemImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=255)
    userid = models.IntegerField()
    user_rank = models.CharField(max_length=255, blank=True)
    starting_price = models.FloatField()
    first_image = models.ForeignKey(ItemImage, default=0, on_delete=models.SET_DEFAULT)
    images = ArrayField(models.IntegerField())