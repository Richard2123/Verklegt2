from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
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
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    itemname = models.CharField(max_length=255)
    condition = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    tag = models.CharField(max_length=50)
    base_price = models.FloatField()
    main_image = models.ImageField(upload_to='storage', null=True, blank=True)
    other_images = ArrayField(models.ImageField(upload_to='images', null=True, blank=True), size=4)
    itemurl = models.SlugField(max_length=100, unique=True)

    def _get_unique_url(self, *args, **kwargs):
        self.itemurl = slugify(self.itemname)
        super(ListItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.itemname} {self.poster} {self.condition} {self.description} {self.itemurl} {self.tag}"

    def __float__(self):
        return self.base_price
