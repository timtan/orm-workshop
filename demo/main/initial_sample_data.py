# coding=utf-8
from __future__ import absolute_import, unicode_literals
import random
import functools

from django.utils.timezone import make_aware
from django.utils import dateparse

from .models import Product, SaleRecord, Channel


random_natural_number = functools.partial(random.randint, 1, 300)


def init_default_data():

    Product.objects.all().delete()
    SaleRecord.objects.all().delete()
    Channel.objects.all().delete()

    p1 = Product.objects.create(name="王紫麵", cost=8)
    p2 = Product.objects.create(name="真由味", cost=18)
    p3 = Product.objects.create(name="湖遲屋", cost=26)
    p4 = Product.objects.create(name="品嗑", cost=38)

    products = [p1, p2, p3, p4]

    c1 = Channel.objects.create(name="加熱福")
    c2 = Channel.objects.create(name="好是多")
    c3 = Channel.objects.create(name="拳家")

    datetime_points = [
        make_aware(dateparse.parse_datetime('2017-07-04 01:01:01')),
        make_aware(dateparse.parse_datetime('2017-10-10 01:01:01')),
        make_aware(dateparse.parse_datetime('2018-01-05 01:01:01')),
        make_aware(dateparse.parse_datetime('2018-04-06 01:01:01')),
        make_aware(dateparse.parse_datetime('2018-07-06 01:01:01')),
    ]

    for product in products:
        for datetime in datetime_points:
            SaleRecord.objects.create(
                product=product,
                channel=c1,
                price=product.cost + 10,
                count=random_natural_number(),
                datetime=datetime,
            )

    for product in products:
        for datetime in datetime_points:
            SaleRecord.objects.create(
                product=product,
                channel=c2,
                price=product.cost * 1.10 ,
                count=random_natural_number(),
                datetime=datetime,
            )

    for product in products:
        for datetime in datetime_points:
            SaleRecord.objects.create(
                product=product,
                channel=c3,
                price=product.cost * 1.40 ,
                count=random_natural_number(),
                datetime=datetime,
            )
