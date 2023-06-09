from django.db import models
from datetime import datetime
from accounts.models import Vendor

class product(models.Model):
    vendor =models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    sport = models.CharField(max_length=100)
    units_remaining = models.IntegerField()
    dimensions = models.CharField(max_length=100)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    sales = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class review(models.Model):
    customer_username = models.CharField(max_length=100)
    Product = models.ForeignKey(product, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=500)
    content = models.TextField()




