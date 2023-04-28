from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>', views.Product, name='product'),
    path('search', views.search, name='search'),
    path('<int:product_id>/delete', views.delete_product, name='delete_product')
]