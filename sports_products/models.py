from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Profile of ' + self.name


class Order(models.Model):

    STATUS_CHOICES = (
        ('A', 'Active'),
        ('C', 'Cancelled')
    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    order_id = models.CharField(max_length=64, unique=True)
    product_name = models.CharField(max_length=512)
    product_url = models.CharField(max_length=1024)
    cost_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return 'Order ID ' + self.order_id
