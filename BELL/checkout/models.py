from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from sellitem.models import ListItem


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(ListItem, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    street_name = models.CharField(max_length=255, null=True)
    house_number = models.IntegerField(null=True)
    city = models.CharField(max_length=255, null=True)
    country = CountryField(max_length=4000, blank_label='(select country)', blank=True)
    postal_code = models.IntegerField(null=True)
    payment_first_name = models.CharField(max_length=255, null=True)
    payment_last_name = models.CharField(max_length=255, null=True)
    card_number = models.IntegerField(null=True)
    card_expiration = models.DateField(null=True)
    card_cvc = models.IntegerField(null=True)




