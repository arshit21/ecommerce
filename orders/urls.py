from django.urls import path
from . import views

urlpatterns = [
    path('add_products', views.add_product, name='add_product'),
    path('<int:product_id>/buy_now', views.buy_now, name='buy_now'),
    path('details', views.export, name="get_details"),
    path('customer/cart', views.shopping_cart, name='cart'),
    path('<int:product_id>/add_to_cart', views.Add_to_Cart, name='add_to_cart'),
    path('customer/cart/<int:cart_object_id>/delete', views.remove_from_cart, name='remove_from_cart'),
    path('customer/cart/buy', views.buy_from_cart, name='buy_from_cart')
]