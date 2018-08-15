# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models

# in real word, money should be decimal field


class Product(models.Model):

    name = models.TextField()
    cost = models.IntegerField()


class Channel(models.Model):

    name = models.TextField()


class SaleRecord(models.Model):

    channel = models.ForeignKey(Channel)
    product = models.ForeignKey(Product)

    price = models.IntegerField()
    count = models.IntegerField(default=0)

    datetime = models.DateTimeField()
