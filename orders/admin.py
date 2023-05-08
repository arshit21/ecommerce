from django.contrib import admin
from .models import order

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'customer_username')
    list_display_links = ('product_title',)

admin.site.register(order, OrdersAdmin)