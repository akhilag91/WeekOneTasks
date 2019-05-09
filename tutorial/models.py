# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length = 40)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
   
class Book(models.Model):
    name = models.CharField(max_length = 30)
    genre = models.CharField(max_length = 20)
    publisher = models.ForeignKey(Publisher)
    published_date = models.DateField()

    def __str__(self):
        return self.name

    