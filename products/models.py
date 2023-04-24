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
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str(self):
        return self.title




