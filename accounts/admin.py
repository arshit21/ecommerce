from django.contrib import admin
from .models import User, Customer, Vendor

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username')

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(User, UserAdmin)


