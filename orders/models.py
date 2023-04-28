from django.db import models
from products.models import product

class order(models.Model):
    customer_username = models.CharField()
    units_ordered = models.IntegerField(default=1)
    Product = models.ManyToManyField(product)
    money = models.IntegerField()
    
    
