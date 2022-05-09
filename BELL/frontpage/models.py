from django.db import models


class Locations(models.Model):
    zip = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.zip}"


class People(models.Model):
    pname = models.CharField(max_length=255)
    location = models.ForeignKey(Locations, default=0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"{self.pname} {self.location}"






