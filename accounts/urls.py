from django.urls import path
from . import views

urlpatterns = [
    path('register/customer', views.register_customer, name='register_customer'),
    path('register/vendor', views.register_vendor, name='register_vendor'),
    path('login', views.login, name='login'),
    path('customer/dashboard', views.customer_dashboard, name='customer_dashboard'),
    path('vendor/dashboard', views.vendor_dashboard, name='vendor_dashboard'),
    path('logout', views.logout, name='logout'),
    path('cutomer/add_money', views.add_money, name='add_money')
]