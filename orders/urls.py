from django.urls import path
from . import views

urlpatterns = [
    path('add_products', views.add_product, name='add_product'),
    path('<int:product_id>/buy_now', views.buy_now, name='buy_now')
]