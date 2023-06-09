from django.urls import path,include
from . import views

urlpatterns = [
    path('register/customer', views.register_customer, name='register_customer'),
    path('register/vendor', views.register_vendor, name='register_vendor'),
    path('login', views.login, name='login'),
    path('customer/dashboard', views.customer_dashboard, name='customer_dashboard'),
    path('vendor/dashboard', views.vendor_dashboard, name='vendor_dashboard'),
    path('logout', views.logout, name='logout'),
    path('customer/add_money', views.add_money, name='add_money'),
    path('vendor/dashboard/placed_orders', views.vendor_orders, name='placed_orders'),
    path('customer/change_address', views.change_address, name='change_address'),
    path('accounts/', include('allauth.urls')),
]