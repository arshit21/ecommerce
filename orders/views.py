from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Vendor
from django.contrib import messages
from .models import order
from products.models import product
from accounts.models import Customer

def add_product(request):
    username = request.user.username
    vendors = Vendor.objects.filter(username=username)[:1]
    for vendor in vendors:
        if request.method == 'POST':
            brand = request.POST['brand']
            title = request.POST['title']
            price = request.POST['price']
            sport = request.POST['sport']
            description = request.POST['description']
            units_remaining = request.POST['units_remaining']
            dimensions = request.POST['dimensions']
            photo_main = request.FILES['photo_main']
            if request.FILES['photo_1']:
                photo_1 = request.FILES['photo_1']
            else:
                photo_1 = None
            if request.FILES['photo_2']:
                photo_2 = request.FILES['photo_2']
            else:
                photo_2 = None
            if request.FILES['photo_3']:
                photo_3 = request.FILES['photo_3']
            else:
                photo_3 = None
            Product = product.objects.create(title=title, brand=brand, price=price, sport=sport, 
                                            description=description, units_remaining=units_remaining, dimensions=dimensions, 
                                            photo_main=photo_main, photo_1=photo_1, photo_2=photo_2, photo_3=photo_3, vendor=vendor)
            Product.save()
            messages.success(request, 'The product has been added')
            return redirect('vendor_dashboard')
    else:
        if request.user.is_vendor:
            return render(request, 'orders/add_products.html')
        else:
            messages.error(request, 'You are not a vendor')
            redirect('index')


def buy_now(request, product_id):
    if request.method == 'POST':
        customer_username = request.user.username
        customers = Customer.objects.filter(username=customer_username)
        Product = get_object_or_404(product, pk=product_id)
        if request.POST['units']:          
            units = request.POST['units']
            units = int(units)
        else:
            units = 1
        price = Product.price
        for customer in customers:
            balance = customer.balance
            balance = int(balance)
            cost = price*units
            if cost > balance:
                messages.error(request, 'Insufficient balance')
                return redirect('product', product_id)
            elif units > Product.units_remaining:
                messages.error(request, 'Out of Stock')
                return redirect('product', product_id)               
            else:
                customer.balance = balance - cost
                Product.units_remaining = Product.units_remaining - units
                Product.sales = Product.sales + units
                Order = order.objects.create(customer_username=customer_username, units_ordered=units, money=cost)
                Order.Product.add(Product)
                Product.save()
                Order.save()
                customer.save()
                messages.success(request, 'The product has been ordered')
                return redirect('index')
                