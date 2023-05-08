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
    
    
