# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers


# Create your models here.
from django.db import models

class User(models.Model):
	email = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	shipping_address = models.CharField(max_length=30)

class Cart(models.Model):
    cart_code = models.CharField(max_length=30)
    total_price = models.DecimalField( max_digits=20, decimal_places=2)
    paid = models.BooleanField()


class Product(models.Model):
    price = models.DecimalField( max_digits=20, decimal_places=2)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)


class Cart_Product(models.Model):
	cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
	product = models.ForeignKey('Product', on_delete=models.CASCADE)


