from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import cart, cart_object, order


class OrdersAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('product_title', 'customer_username')
    list_display_links = ('product_title',)

class CartsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('customer_username',)
    list_display_links = ('customer_username',)

class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_username')
    list_display_links = ('id',)

admin.site.register(order, OrdersAdmin)
admin.site.register(cart, CartsAdmin)
admin.site.register(cart_object, ObjectsAdmin)
