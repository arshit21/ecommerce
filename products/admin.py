from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import product, review

class productAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'vendor', 'list_date')
    list_display_links = ('title',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 25
admin.site.register(product, productAdmin)

class reviewAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'Product', 'customer_username', )
    list_display_links = ('id', 'title')

admin.site.register(review, reviewAdmin)