from django.contrib import admin
from .models import product

class productAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'vendor', 'list_date')
    list_display_links = ('title',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 25
admin.site.register(product, productAdmin)