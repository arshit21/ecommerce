from django.contrib import admin
from .models import User, Customer, Vendor

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(User)


