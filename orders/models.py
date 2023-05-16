from django.db import models
from datetime import datetime
from products.models import product

class order(models.Model):
    customer_username = models.CharField()
    vendor_username = models.CharField(blank=True)
    units_ordered = models.IntegerField(default=1)
    Product = models.ManyToManyField(product)
    product_title = models.CharField(blank=True)
    product_id = models.IntegerField(blank=True)
    money = models.IntegerField()
    order_date = models.DateTimeField(default=datetime.now, blank=True)

class cart_object(models.Model):
    customer_username = models.CharField(blank=True)
    Product = models.ManyToManyField(product, blank=True)
    units = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)

class cart(models.Model):
    customer_username = models.CharField()
    item = models.ManyToManyField(cart_object, blank=True)
    money = models.IntegerField(default=0)

class wishlist(models.Model):
    customer_username = models.CharField()
    Product = models.ManyToManyField(product, blank=True)
    price = models.IntegerField(blank=True)