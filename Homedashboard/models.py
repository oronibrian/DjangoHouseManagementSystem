from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import Model


class HouseCategory(models.Model):
    category = models.CharField(max_length=155)


    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural ='HouseCategories'

class Price(models.Model):
    price = models.IntegerField()
    category = models.ForeignKey(HouseCategory, default=6000)

    def __unicode__(self):
      return str(self.price)


class House(models.Model):
    roomno = models.IntegerField(primary_key=True)
    floor = models.CharField(max_length=32)
    status = models.TextField()
    category = models.ForeignKey(HouseCategory,default=6000)


    def __str__(self):
        return self.status



class Tenant(models.Model):
    firstname = models.CharField(max_length=255)
    secondname = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.CharField(max_length=255)
    roomnumber = models.IntegerField()
    nooftenant = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname







