from django.db import models
from django.contrib.postgres.fields import ArrayField


class ListItem(models.Model):
    userid = models.IntegerField()
    itemname = models.CharField(max_length=255)
    condition = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    base_price = models.FloatField()
    main_image = models.IntegerField()
    other_images = ArrayField(models.IntegerField())
