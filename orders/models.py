from django.db import models
from datetime import datetime
from products.models import product

class order(models.Model):
    customer_username = models.CharField(max_length=100)
    vendor_username = models.CharField(max_length=100, blank=True)
    units_ordered = models.IntegerField(default=1)
    Product = models.ManyToManyField(product)
    product_title = models.CharField(max_length=200, blank=True)
    product_id = models.IntegerField(blank=True)
    money = models.IntegerField()
    order_date = models.DateTimeField(default=datetime.now, blank=True)

class cart_object(models.Model):
    customer_username = models.CharField(max_length=100, blank=True)
    Product = models.ManyToManyField(product, blank=True)
    units = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)

class cart(models.Model):
    customer_username = models.CharField(max_length=100)
    item = models.ManyToManyField(cart_object, blank=True)
    money = models.IntegerField(default=0)

class wishlist(models.Model):
    customer_username = models.CharField(max_length=100)
    Product = models.ManyToManyField(product, blank=True)
    price = models.IntegerField(blank=True)