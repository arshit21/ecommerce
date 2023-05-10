from django.contrib import admin
from .models import order, cart, cart_object

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'customer_username')
    list_display_links = ('product_title',)

class CartsAdmin(admin.ModelAdmin):
    list_display = ('customer_username',)
    list_display_links = ('customer_username',)

class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_username')
    list_display_links = ('id',)

admin.site.register(order, OrdersAdmin)
admin.site.register(cart, CartsAdmin)
admin.site.register(cart_object, ObjectsAdmin)
